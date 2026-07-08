from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

from models import db
from models.opportunity import Opportunity

from datetime import datetime

opportunity = Blueprint("opportunity", __name__)


@opportunity.route("/add-opportunity", methods=["GET", "POST"])
@login_required
def add_opportunity():

    if request.method == "POST":

        title = request.form["title"]
        company = request.form["company"]
        category = request.form["category"]
        deadline = request.form["deadline"]
        link = request.form["link"]
        description = request.form["description"]

        new_opportunity = Opportunity(
            title=title,
            company=company,
            category=category,
            deadline=datetime.strptime(deadline, "%Y-%m-%d").date(),
            link=link,
            description=description,
            user_id=current_user.id
        )

        db.session.add(new_opportunity)
        db.session.commit()

        flash("Opportunity added successfully!", "success")

        return redirect(url_for("dashboard.dashboard_home"))

    return render_template(
        "add_opportunity.html", 
        opportunity=None, 
        button_text="Save Opportunity"
        )

@opportunity.route("/opportunities")
@login_required
def view_opportunities():

    opportunities = Opportunity.query.filter_by(
        user_id=current_user.id
    ).all()

    return render_template(
        "opportunities.html",
        opportunities=opportunities
    )

@opportunity.route("/edit-opportunity/<int:id>", methods=["GET", "POST"])
@login_required
def edit_opportunity(id):

    opportunity = Opportunity.query.get_or_404(id)

    if opportunity.user_id != current_user.id:
        flash("Unauthorized Access!", "danger")
        return redirect(url_for("opportunity.view_opportunities"))

    if request.method == "POST":

        opportunity.title = request.form["title"]
        opportunity.company = request.form["company"]
        opportunity.category = request.form["category"]
        opportunity.deadline = datetime.strptime(
            request.form["deadline"],
            "%Y-%m-%d"
        ).date()

        opportunity.link = request.form["link"]
        opportunity.description = request.form["description"]

        db.session.commit()

        flash("Opportunity updated successfully!", "success")

        return redirect(url_for("opportunity.view_opportunities"))

    return render_template(
        "edit_opportunity.html",
        opportunity=opportunity,
        button_text="Update Opportunity"
    )

@opportunity.route("/delete-opportunity/<int:id>", methods=["POST"])
@login_required
def delete_opportunity(id):

    opportunity = Opportunity.query.get_or_404(id)

    if opportunity.user_id != current_user.id:
        flash("Unauthorized Access!", "danger")
        return redirect(url_for("opportunity.view_opportunities"))

    db.session.delete(opportunity)
    db.session.commit()

    flash("Opportunity deleted successfully!", "success")

    return redirect(url_for("opportunity.view_opportunities"))