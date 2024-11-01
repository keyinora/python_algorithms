def decayed_followers(intl_followers, fraction_lost_daily, days):
    retention_rate = 1.0 - fraction_lost_daily
    return intl_followers * (retention_rate ** days)
