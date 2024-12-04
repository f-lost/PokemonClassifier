import preprocess
import training
import evaluate

filename = 'Pokemon.csv'
batch_size = 32
epochs = 200

X_train, X_test, y_train, y_test = preprocess.preprocess(filename)

model = training.training(
                batch_size, 
                epochs,
                X_train,
                X_test,
                y_train,
                y_test
                )

evaluate.evaluate(model, X_train, X_test, y_train, y_test)
