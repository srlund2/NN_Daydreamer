##HAVE TO USE THIS IM JUST THROWING IT IN INCASE IT IS HELPFUL


dataset = torchvision.datasets.MNIST(root="mnist/", train=True, download=True, transform=Compose([
              torchvision.transforms.ToTensor(),
              torchvision.transforms.Lambda(lambda t: (t * 2) - 1)]))
train_dataloader = DataLoader(dataset, batch_size=128, shuffle=True)

