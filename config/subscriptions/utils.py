from .models import Subscription


def get_user_plan(user):
    try:
        return user.subscription.plan
    except Subscription.DoesNotExist:
        return None


def can_create_project(user):
    plan = get_user_plan(user)
    if not plan:
        return False
    current_count = user.owned_projects.count()
    return current_count < plan.max_projects


def can_create_organization(user):
    plan = get_user_plan(user)
    if not plan:
        return False
    current_count = user.owned_organizations.count()
    return current_count < plan.max_organizations


def can_create_task(user, project):
    plan = get_user_plan(user)
    if not plan:
        return False
    current_count = project.tasks.count()
    return current_count < plan.max_tasks