from ai_modules.scikit_decision import predict_state_scikit
from ai_modules.tensorflow_decision import predict_state_tensorflow
from ai_modules.pytorch_decision import predict_state_pytorch

def vote(file_path, indicatorDataObj):
    count = 0
    print("scikit starting")
    scikit_result = predict_state_scikit(file_path, indicatorDataObj)
    print("result = " + scikit_result)
    print("tensorflow starting")
    _, tensorflow_result = predict_state_tensorflow(file_path, indicatorDataObj)
    print("tensorflow result = " + tensorflow_result)
    print("pytorch starting")
    pytorch_result = predict_state_pytorch(file_path, indicatorDataObj)
    print("pytorch result = " + pytorch_result)
    
    if scikit_result == "LONG":
        count = count + 1
    if tensorflow_result == "LONG":
        count = count + 1
    if pytorch_result == "LONG":
        count = count + 1

    if count >= 2:
        return scikit_result, tensorflow_result, pytorch_result, "LONG"
    else:
        return scikit_result, tensorflow_result, pytorch_result, "SHORT"
