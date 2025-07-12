from markov_core import MarkovChain

mc = MarkovChain(3)

mc.train("training_data.txt")

mc.to_json("model_3rd_order.json")

print("3rd-order Markov Chain trained and saved.")
