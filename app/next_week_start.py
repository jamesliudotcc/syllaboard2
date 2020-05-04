from typing import Optional
from datetime import date, timedelta
import holidays


def next_week_start(iso_date: Optional[str] = None) -> date:
    """
    Returns the next start of week from today, or if an iso date string
    is supplied, from that date. Usually returns Monday. Implements US
    holidays, i18n is to do.
    """
    if iso_date:
        current_date = date.fromisoformat(iso_date)
    else:
        current_date = date.today()

    days_until_monday = 7 - current_date.weekday()

    candidate_start = current_date + timedelta(days=days_until_monday)
    while candidate_start in holidays.US():
        candidate_start += timedelta(days=1)

    return candidate_start
