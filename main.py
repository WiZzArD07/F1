import fastf1
import pandas as pd

# Enable cache (VERY IMPORTANT for speed)
fastf1.Cache.enable_cache('cache')

def load_race(year=2024, gp="Monaco"):
    print(f"Loading {gp} {year} Race...")

    session = fastf1.get_session(year, gp, 'R')
    session.load()

    print("✅ Session loaded successfully!\n")

    return session


def show_basic_info(session):
    print("📊 Drivers:")
    print(session.drivers)

    print("\n📊 Sample Laps Data:")
    print(session.laps.head())

    print("\n📊 Weather Data:")
    print(session.weather_data.head())


def get_driver_telemetry(session, driver_code="VER"):
    print(f"\n📡 Getting telemetry for {driver_code}...")

    driver_laps = session.laps.pick_driver(driver_code)

    fastest_lap = driver_laps.pick_fastest()

    telemetry = fastest_lap.get_telemetry()

    print("\n📊 Telemetry Sample:")
    print(telemetry[['Speed', 'Throttle', 'Brake', 'nGear']].head())

    return telemetry


if __name__ == "__main__":
    session = load_race(2024, "Monaco")

    show_basic_info(session)

    telemetry = get_driver_telemetry(session, "VER")