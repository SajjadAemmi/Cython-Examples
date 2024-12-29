#include <opencv2/opencv.hpp>
#include <iostream>
#include <chrono>

using namespace std;
using namespace cv;

void applyConvolution(const Mat &image, Mat &output, const int kernel[3][3])
{
    for (int i = 1; i < image.rows - 1; ++i)
    {
        for (int j = 1; j < image.cols - 1; ++j)
        {
            int pixel_sum = 0;
            for (int ki = -1; ki <= 1; ++ki)
            {
                for (int kj = -1; kj <= 1; ++kj)
                {
                    pixel_sum += kernel[ki + 1][kj + 1] * image.at<uchar>(i + ki, j + kj);
                }
            }
            output.at<uchar>(i, j) = saturate_cast<uchar>(pixel_sum);
        }
    }
}

int main()
{
    Mat image = imread("../../assets/lion-king.jpg", IMREAD_GRAYSCALE);
    Mat output = Mat::zeros(image.size(), CV_8U);

    int kernel[3][3] = {
        {1, 0, -1},
        {1, 0, -1},
        {1, 0, -1}};

    auto start_time = chrono::high_resolution_clock::now();
    applyConvolution(image, output, kernel);
    auto end_time = chrono::high_resolution_clock::now();

    chrono::duration<double> elapsed_time = end_time - start_time;
    cout << "Convolution Time (C++): " << elapsed_time.count() << " seconds" << endl;
    imwrite("output_cpp.jpg", output);
    return 0;
}
