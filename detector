import cv2
import mediapipe as mp
import math

# Initialize MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

mp_drawing = mp.solutions.drawing_utils
drawing_spec = mp_drawing.DrawingSpec(color=(0,255,0), thickness=1, circle_radius=1)

# Landmarks for eyes and mouth (MediaPipe 468 points)
LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]
OUTER_LIPS = [61, 291, 78, 308, 13, 14, 312, 82]

# Function to calculate EAR
def eye_aspect_ratio(landmarks, eye_indices):
    a = math.dist(landmarks[eye_indices[1]], landmarks[eye_indices[5]])
    b = math.dist(landmarks[eye_indices[2]], landmarks[eye_indices[4]])
    c = math.dist(landmarks[eye_indices[0]], landmarks[eye_indices[3]])
    ear = (a + b) / (2.0 * c)
    return ear

# Function to calculate MAR
def mouth_aspect_ratio(landmarks, lip_indices):
    a = math.dist(landmarks[lip_indices[0]], landmarks[lip_indices[6]])
    b = math.dist(landmarks[lip_indices[1]], landmarks[lip_indices[5]])
    c = math.dist(landmarks[lip_indices[2]], landmarks[lip_indices[4]])
    mar = (a + b + c) / 3.0
    return mar

# Head tilt / roll
def head_roll_angle(landmarks):
    left_eye_center = landmarks[33]
    right_eye_center = landmarks[263]
    dy = right_eye_center[1] - left_eye_center[1]
    dx = right_eye_center[0] - left_eye_center[0]
    angle = math.degrees(math.atan2(dy, dx))
    return angle

# Start camera
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Camera not found!")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(frame_rgb)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            h, w, c = frame.shape
            landmarks = [(int(lm.x*w), int(lm.y*h)) for lm in face_landmarks.landmark]

            # Draw mesh
            mp_drawing.draw_landmarks(
                frame, face_landmarks, mp_face_mesh.FACEMESH_TESSELATION,
                landmark_drawing_spec=None,
                connection_drawing_spec=drawing_spec
            )

            # Eyes EAR
            left_ear = eye_aspect_ratio(landmarks, LEFT_EYE)
            right_ear = eye_aspect_ratio(landmarks, RIGHT_EYE)
            eye_status = "OPEN" if (left_ear + right_ear)/2 > 0.25 else "CLOSED"

            # Mouth MAR
            mar = mouth_aspect_ratio(landmarks, OUTER_LIPS)
            mouth_status = "OPEN" if mar > 0.05 else "CLOSED"  # threshold can adjust

            # Head roll
            roll = head_roll_angle(landmarks)

            # Display status
            cv2.putText(frame, f"Eyes: {eye_status}", (30,30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0) if eye_status=="OPEN" else (0,0,255), 2)
            cv2.putText(frame, f"Mouth: {mouth_status}", (30,60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,255) if mouth_status=="OPEN" else (255,0,0), 2)
            cv2.putText(frame, f"Head Roll: {roll:.1f} deg", (30,90), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,255), 2)

    cv2.imshow("Face + Eyes + Mouth + Head Level", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
