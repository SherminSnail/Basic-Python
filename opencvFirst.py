import cv2 as cv2
print(cv2.__version__)
import sys

def main():
    # Path to the image file
    image_path = r"C:\Users\FB-EET-Loan\Pictures\Screenshots\example.png"

    # Try to read the image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not load image from '{r"C:\Users\FB-EET-Loan\Pictures\Screenshots"}'.")
        sys.exit(1)

    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Display the original and grayscale images
    cv2.imshow("Original Image", image)
    cv2.imshow("Grayscale Image", gray_image)

    # Wait for a key press and close windows
    print("Press any key to close the windows...")
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
