import cv2
import sys

cap = cv2.VideoCapture(0)

def selectROIfromFrame(frame):
    # box (x, y, lar, alt)
    box = cv2.selectROI("SELECT ROI", frame, fromCenter=False, showCrosshair=False)
    print(box)
    return box
first_frame = cv2.imread("MinhaMao.jpeg")
#box = selectROIfromFrame(first_frame)#executei e peguei os resultados
box = (19, 47, 204, 393)
if __name__ == "__main__":
    camera,frame = cap.read()

    tracker = cv2.TrackerCSRT_create()
    ok = tracker.init(first_frame, box)
    while cap.isOpened():
        ret, frame = cap.read()
        ok, box = tracker.update(frame)
        if ok:
            pt1 = (box[0], box[1])
            pt2 = ((box[0] + box[2]), (box[1] + box[3]))
            cv2.rectangle(frame, pt1, pt2, (255, 0, 0), 2)
            print("X=",(box[0] + box[2]),"Y=",(box[1] + box[3])/2,"Dist=")
        else:
            print("FALHOU")
        cv2.imshow("Tracking", frame)
        if cv2.waitKey(1) == ord('f'):   break
    cap.realease()
    cv2.destroyAllWindows()