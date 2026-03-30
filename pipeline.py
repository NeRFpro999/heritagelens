import cv2
import numpy as np
# import open3d as o3d  # Note: Open3D may need separate installation
import os

def process_images(image_paths, output_dir):
    """
    Process uploaded images: save originals and apply Canny edge detection to create processed versions.
    Saves images in output_dir/images/
    """
    images_dir = os.path.join(output_dir, "images")
    os.makedirs(images_dir, exist_ok=True)

    processed_paths = []
    for i, img_path in enumerate(image_paths):
        # Read image
        img = cv2.imread(img_path)
        if img is None:
            continue

        # Save original
        original_path = os.path.join(images_dir, f"original_{i}.jpg")
        cv2.imwrite(original_path, img)

        # Apply Canny edge detection
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 100, 200)
        processed_path = os.path.join(images_dir, f"processed_{i}.jpg")
        cv2.imwrite(processed_path, edges)

        processed_paths.append(processed_path)

    return processed_paths

def generate_point_cloud(image_paths, output_dir):
    """
    Generate a sparse point cloud from images using ORB feature matching and triangulation.
    Saves point cloud as point_cloud.ply in output_dir
    Note: This requires Open3D. If not installed, this will be skipped.
    """
    try:
        import open3d as o3d
    except ImportError:
        print("Open3D not installed. Skipping point cloud generation.")
        return None

    # This is a simplified implementation for MVP. In a real app, use proper SfM libraries.

    # Load images
    images = []
    for path in image_paths:
        img = cv2.imread(path)
        if img is not None:
            images.append(img)

    if len(images) < 2:
        return None

    # Use Open3D's reconstruction pipeline (simplified)
    # For MVP, create a basic point cloud from features

    # Initialize ORB detector
    orb = cv2.ORB_create()

    # Detect keypoints and descriptors for first two images
    kp1, des1 = orb.detectAndCompute(images[0], None)
    kp2, des2 = orb.detectAndCompute(images[1], None)

    # Match descriptors
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda x: x.distance)

    # Extract matched points
    pts1 = np.float32([kp1[m.queryIdx].pt for m in matches])
    pts2 = np.float32([kp2[m.trainIdx].pt for m in matches])

    # Assume simple camera parameters for triangulation
    # In reality, need proper calibration
    focal_length = 1000  # pixels
    cx, cy = images[0].shape[1] / 2, images[0].shape[0] / 2

    # Create projection matrices (simplified)
    K = np.array([[focal_length, 0, cx], [0, focal_length, cy], [0, 0, 1]])
    P1 = np.hstack((K, np.zeros((3, 1))))
    P2 = np.hstack((K, np.array([[0], [0], [100]])))  # Assume translation

    # Triangulate points
    pts4D = cv2.triangulatePoints(P1, P2, pts1.T, pts2.T)
    pts3D = pts4D[:3] / pts4D[3]

    # Create Open3D point cloud
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(pts3D.T)

    # Save point cloud
    ply_path = os.path.join(output_dir, "point_cloud.ply")
    o3d.io.write_point_cloud(ply_path, pcd)

    return ply_path