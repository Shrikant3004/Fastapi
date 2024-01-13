import asyncio
import cv2
from aiortc import RTCPeerConnection, RTCSessionDescription, VideoStreamTrack

# Create a video track using OpenCV
class VideoStream(VideoStreamTrack):
    def __init__(self):
        super().__init__()
        self.cap = cv2.VideoCapture(0)  # Initialize OpenCV video capture (change the index for different cameras)
        self.frame_width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.frame_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    async def recv(self):
        while True:
            ret, frame = self.cap.read()  # Read frame from OpenCV capture

            if not ret:
                break

            # Convert OpenCV BGR frame to RGB
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Reshape the frame to fit aiortc requirements
            pts, time_base = await self.next_timestamp()
            frame_time = pts / time_base
            self.track.frame(frame_rgb, frame_time)
            await asyncio.sleep(0)

    async def stop(self):
        self.cap.release()

async def create_peer_connection():
    # Initialize the peer connection
    pc = RTCPeerConnection()

    # Add the video stream track
    video_track = VideoStream()
    pc.addTrack(video_track)

    # Create an offer
    offer = await pc.createOffer()
    await pc.setLocalDescription(offer)

    # Print the offer SDP (for demonstration purposes)
    print("Offer SDP:")
    print(pc.localDescription.sdp)

    # Close the peer connection when done
    await pc.close()
    await video_track.stop()

async def main():
    # Run the peer connection creation
    await create_peer_connection()

# Run the main coroutine
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
