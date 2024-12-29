#include <stdio.h>
#include <stdlib.h>
#include <tensorflow/c/c_api.h>
#include <time.h>

void DeallocateBuffer(void *data, size_t length, void *arg)
{
    free(data);
}

TF_Tensor *CreateRandomTensor(int rows, int cols)
{
    // Allocate memory for the tensor
    float *data = (float *)malloc(rows * cols * sizeof(float));

    // Populate the tensor with random values
    for (int i = 0; i < rows * cols; i++)
    {
        data[i] = ((float)rand() / (float)RAND_MAX) * 10.0f; // Random float between 0 and 10
    }

    // Create a TensorFlow tensor
    int64_t dims[2] = {rows, cols};
    TF_Tensor *tensor = TF_NewTensor(TF_FLOAT, dims, 2, data, rows * cols * sizeof(float), DeallocateBuffer, NULL);

    return tensor;
}

void PrintTensor(TF_Tensor *tensor, int rows, int cols)
{
    float *data = (float *)TF_TensorData(tensor);
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            printf("%f ", data[i * cols + j]);
        }
        printf("\n");
    }
}

int main()
{
    // Start clock
    clock_t start_time = clock();

    // Set up TensorFlow session options
    TF_Status *status = TF_NewStatus();

    // Create two random tensors
    int rows = 20000, cols = 20000;
    TF_Tensor *tensor1 = CreateRandomTensor(rows, cols);

    // Clean up
    TF_DeleteTensor(tensor1);
    TF_DeleteStatus(status);

    // End clock
    clock_t end_time = clock();

    // Calculate and print process time in seconds
    double elapsed_time = (double)(end_time - start_time) / CLOCKS_PER_SEC;
    printf("Process time: %f seconds\n", elapsed_time);

    return 0;
}
