from flask import Blueprint, render_template
from flask_login import login_required, current_user

from models.opportunity import Opportunity

dashboard = Blueprint("dashboard", __name__)


@dashboard.route("/dashboard")
@login_required
def dashboard_home():

    total_opportunities = Opportunity.query.filter_by(
        user_id=current_user.id
    ).count()

    return render_template(
        "dashboard.html",
        user=current_user,
        total_opportunities=total_opportunities
    )