import Function_Library as fl
import cv2

EPOCH = 500000

if __name__ == "__main__":
    # Exercise Environment Setting
    env = fl.libCAMERA()

    # Camera Initial Setting (단일 카메라로 변경)
    ch0, ch1 = env.initial_setting(cam0port=0, capnum=1)

    try:
        # Camera Reading..
        for i in range(EPOCH):
            _, frame0 = env.camera_read(ch0)

            """ Webcam Real-time Reading """
            ############## YOU MUST EDIT ONLY HERE ##############
            env.image_show(frame0)
            #####################################################

            """ Object Detection (Traffic Light Circle) """
            #################### YOU MUST EDIT ONLY HERE ####################
            #color = env.object_detection(frame0, sample=16, print_enable=True)
            #################################################################

            # Process Termination (If you input the 'q', camera scanning is ended.)
            if env.loop_break():
                break

    except KeyboardInterrupt:
        print("Program interrupted by user")

    finally:
        # 카메라 리소스 해제
        if ch0 is not None:
            ch0.release()
        if ch1 is not None:
            ch1.release()
        cv2.destroyAllWindows()
        print("Camera resources released")