import pygetwindow as gw
import pyautogui
import cv2
import numpy as np
import time

# Set the region to capture (you can adjust these values)
left, top, width, height = 0, 0, 1920, 1080

# Set the output video file name
output_file = 'screen_recording.mp4'

# Get the screen resolution
screen = gw.getWindowsWithTitle('')[0]
screen_width, screen_height = screen.width, screen.height

# Create a video writer object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_file, fourcc, 20.0, (width, height))

# Main recording loop
try:
    while True:
        # Capture the screen
        screenshot = pyautogui.screenshot(region=(left, top, width, height))
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # Write the frame to the video file
        out.write(frame)

        # Optional: Display the recording in a window
        cv2.imshow('Screen Recording', frame)

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    pass

finally:
    # Release the video writer and close the window
    out.release()
    cv2.destroyAllWindows()
