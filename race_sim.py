import arcade
import fastf1
import os
import random

# -------------------------------
# Setup Cache
# -------------------------------
os.makedirs("cache", exist_ok=True)
fastf1.Cache.enable_cache("cache")

print("Loading session...")
session = fastf1.get_session(2024, "Monaco", "R")
session.load()
print(" Session loaded!")

# -------------------------------
# Load Drivers
# -------------------------------
drivers = session.drivers[:5]

driver_data = {}

for drv in drivers:
    try:
        laps = session.laps.pick_drivers(drv)
        fastest = laps.pick_fastest()
        tel = fastest.get_telemetry()

        driver_data[drv] = {
            "X": tel['X'].values[::5],
            "Y": tel['Y'].values[::5],
            "color": (
                random.randint(100, 255),
                random.randint(100, 255),
                random.randint(100, 255)
            ),
            "offset": random.randint(0, 200)
        }
    except:
        continue

print("Drivers loaded:", list(driver_data.keys()))

# -------------------------------
# Normalize
# -------------------------------
sample = list(driver_data.values())[0]
X = sample["X"]
Y = sample["Y"]

min_x, max_x = min(X), max(X)
min_y, max_y = min(Y), max(Y)

def normalize(x, y):
    x = (x - min_x) / (max_x - min_x) * 700 + 50
    y = (y - min_y) / (max_y - min_y) * 700 + 50
    return x, y


# -------------------------------
# Window
# -------------------------------
class F1Replay(arcade.Window):
    def __init__(self):
        super().__init__(800, 800, "F1 Replay ")
        arcade.set_background_color(arcade.color.BLACK)
        self.frame = 0

    def on_draw(self):
        self.clear()

        # Draw track
        for i in range(len(X) - 1):
            dx = abs(X[i+1] - X[i])
            dy = abs(Y[i+1] - Y[i])

            # Skip unrealistic jumps
            if dx > 1000 or dy > 1000:
             continue
            x1, y1 = normalize(X[i], Y[i])
            x2, y2 = normalize(X[i + 1], Y[i + 1])

            arcade.draw_line(x1, y1, x2, y2, arcade.color.WHITE, 2)
        # Close the loop (important)
        x1, y1 = normalize(X[-1], Y[-1])
        x2, y2 = normalize(X[0], Y[0])
        arcade.draw_line(x1, y1, x2, y2, arcade.color.WHITE, 2)

        # Draw cars
        for drv, data in driver_data.items():

            # base index (must be int)
            base = int(self.frame + data["offset"]) % len(data["X"])
            next_idx = (base + 1) % len(data["X"])

            # interpolation factor (decimal part)
            t = (self.frame % 1)

            # interpolate between two points
            x = (1 - t) * data["X"][base] + t * data["X"][next_idx]
            y = (1 - t) * data["Y"][base] + t * data["Y"][next_idx]

            cx, cy = normalize(x, y)

            arcade.draw_circle_filled(cx, cy, 10, data["color"])
        
    def on_update(self, delta_time):
        self.frame += 0.2   

        #  FORCE SCREEN REFRESH
        self.on_draw()


# -------------------------------
# Run
# -------------------------------
if __name__ == "__main__":
    window = F1Replay()
    arcade.run()