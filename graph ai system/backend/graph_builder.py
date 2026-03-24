import networkx as nx
import pandas as pd

def build_graph():
    G = nx.DiGraph()
    data = pd.read_csv("../data/sample_data.csv")

    for _, row in data.iterrows():
        G.add_node(row["order"], type="order")
        G.add_node(row["product"], type="product")
        G.add_node(row["customer"], type="customer")

        G.add_edge(row["customer"], row["order"])
        G.add_edge(row["order"], row["product"])

    return G
