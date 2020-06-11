# TorchServe MNIST example

In this example, we show how to use a pre-trained custom MNIST model to performing real time Digit recognition with TorchServe. The inference service would return the digit inferred by the model in the input image. This example is taken directly drom the TorchServe repo, [here](https://github.com/pytorch/serve/tree/master/examples/image_classifier/mnist).

## Setup

First, we need to create a new conda environment to install the dependencies.

```
conda create -n torch python=3.8
```

Activate the environment with `conda activate torch`.

Second, install the PyTorch ecosystem. (This command installs only the CPU version)

```
conda install pytorch torchvision torchtext torchserve torch-model-archiver psutil future cpuonly -c pytorch -c powerai
```

Finally, clone the repo to your machine.

```
git clone https://github.com/dpoulopoulos/medium.git
```

## Serve the model

`cd` into the `torch_serve` folder and run the following commands:

- Create a torch model archive using the torch-model-archiver utility. This command archives the provided model (artefacts/model.pt) into a .mar file. If you want to train a model yourself run the `main.py` script. Run `python main.py -h` to see a list of available arguments.

```
torch-model-archiver --model-name mnist --version 1.0 --model-file model.py --serialized-file artefacts/model.pt --handler handler.py
```

- Create a `model_store` folder and move the file inside.

```
mkdir model_store
mv mnist.mar model_store/
```
- Start the server and serve the model.

```
torchserve --start --model-store model_store --models mnist=mnist.mar
```

- Make predictions.

```
curl http://127.0.0.1:8080/predictions/mnist -T test_data/0.png
```

- When you are done, stop the server.

```
torchserve --stop
```