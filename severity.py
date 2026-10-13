def classify_severity(area):
    """
    Classify pothole severity based on bounding-box area.
    """

    if area < 5000:
        return "Low"
    elif area < 15000:
        return "Medium"
    else:
        return "High"


def road_condition_score(total_potholes, severity_list):
    """
    Calculate road health score out of 100.
    Higher pothole count and severity reduce the score.
    """

    score = 100

    # Deduct based on pothole count
    score -= total_potholes * 2

    # Deduct based on severity
    for severity in severity_list:

        if severity == "Low":
            score -= 3

        elif severity == "Medium":
            score -= 7

        elif severity == "High":
            score -= 15

    return max(0, score)