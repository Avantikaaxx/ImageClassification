#Importing dependencies
import torch
import torchvision.models as models
from torchvision import transforms
from PIL import Image

def pred_image(IMAGE_PATH):
    PATH       = 'model_best.pth.tar'
    IMAGE_PATH = 'uploads/'+ str(IMAGE_PATH)
    labels     = ['custard_apple', 'kite', 'koala','Scottish_deerhound' ,'Irish_wolfhound' ]


    #Below steps include:
    #Loading the pre-trained model
    #Making predictions
    #Taking outputs
    model  = models.alexnet()
    optimizer = torch.optim.SGD(model.parameters(), 0.01,
                                    momentum=0.9,
                                    weight_decay=1e-4)
    model.features = torch.nn.DataParallel(model.features)
    #model.cuda()
    model  = models.alexnet(pretrained = True)
    model.eval()
    #Transforming the input image
    transform = transforms.Compose([transforms.Resize(256),
                                    transforms.CenterCrop(224),                
                                    transforms.ToTensor(),                     
                                    transforms.Normalize(mean=[0.485, 0.456, 0.406],               
                                                        std=[0.229, 0.224, 0.225])
                                    ])
    img = Image.open(IMAGE_PATH)
    img_t = transform(img)
    batch_t = torch.unsqueeze(img_t, 0)

    labels = ['custard_apple', 'kite', 'koala','Scottish_deerhound' ,'Irish_wolfhound' ]

    #Making Prediction
    out = model(batch_t)
    _, index = torch.max(out, 1)

    percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100

    res = ''

    f=open('imagenet_classes_index.txt')
    lines=f.readlines()
    res = lines[index[0]].split(',')[1].strip() +"confidence % of the Input Image:"+  str( percentage[index[0]].item())[:4]
    f.close()
    
    return(res)
