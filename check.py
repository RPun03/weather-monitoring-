def check_alert_conditions(data):
    temp_celsius = data["main"]["temp"]

    # Example: trigger an alert if temperature exceeds 35°C
    if temp_celsius > 35:
        print(f"Alert: Temperature in {data['name']} exceeds 35°C!")
        # Optionally: send an email or log this alert
