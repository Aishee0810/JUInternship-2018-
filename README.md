# JUInternship-2018-
Project on "Hand Gesture Recognition using 2D Depth Images"
I mainly dealt with the preprocessing of the images, where I had to use OpenCV Python and Computer Vision techniques.I
have also studied deep learning algorithms , and used Weka to classify the datasets, using Random
Forest Classifier.
There were two types of Datasets for the images, A and B. The images were extremely noisy, and the hand contours could not be detected at all. To solve this problem,
I plotted the histogram for a sample of the images, and found the pixel intensity to be in a range of 2-3. Hence, for every image, I set the pixel corresponding to
intensity 3 as 255, and 0 otherwise. I also used Bilateral Filters to remove noise. This folder contains the codes for the same. The different files for different
datasets A and B correspond to images whose pixel intensity was a bit different from 3, and had to be coded in separately.
