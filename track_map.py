import fastf1
import matplotlib.pyplot as plt
import os

# -------------------------------
# Setup Cache (auto create)
# -------------------------------
cache_dir = "cache"
os.makedirs(cache_dir, exist_ok=True)
fastf1.Cache.enable_cache(cache_dir)

print("Loading session...")

# -------------------------------
# Load Race Session
# -------------------------------
session = fastf1.get_session(2024, "Monaco", "R")
session.load()

print("✅ Session loaded!")

# -------------------------------
# Get Fastest Lap Telemetry
# -------------------------------
lap = session.laps.pick_fastest()
tel = lap.get_telemetry()

x = tel['X']
y = tel['Y']

print("Telemetry loaded!")

# -------------------------------
# Plot Track
# -------------------------------
plt.figure(figsize=(8, 8), facecolor='black')

plt.plot(x, y, color='cyan', linewidth=2)

ax = plt.gca()
ax.set_facecolor('black')

plt.title("Monaco Track Map", color='white')
plt.axis('off')

# -------------------------------
# Save Image (IMPORTANT)
# -------------------------------
plt.savefig("track.png", dpi=300, bbox_inches='tight')
print("✅ Track saved as track.png")

# -------------------------------
# Optional: Show Window
# -------------------------------
try:
    plt.show()
except:
    print("⚠️ GUI not supported, open track.png manually")