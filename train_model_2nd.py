from markov_core import MarkovChain

mc = MarkovChain(2)

mc.train("training_data.txt")

mc.to_json("model_2nd_order.json")

print("Training complete. Model saved.")
