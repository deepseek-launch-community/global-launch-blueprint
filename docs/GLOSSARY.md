# Glossary of Core Terms
*Brief explanations of key concepts central to our project discussions.*

### Mixture of Experts (MoE)
A neural network architecture where the model consists of many "expert" sub-networks, and a "router" decides which experts to use for each input token.

### Router
The component in an MoE model that takes a token‘s representation and outputs a probability distribution over the available experts.

### Adaptive-K Routing
A dynamic routing strategy where the number of experts (K) selected per token is not fixed, but determined based on the router‘s confidence (entropy) for that token.

### Entropy (in this context)
A measure of the uncertainty or dispersion of the router‘s probability distribution. **Low entropy** means the router is confident (one expert has high probability). **High entropy** means the router is uncertain (probabilities are more evenly spread).

### Load Balancing
The challenge in MoE training of ensuring all experts receive a roughly equal amount of training data, preventing some experts from being underused.

---
*This glossary is a living document and will be updated as the project evolves.*


# 核心术语表
*对本项目讨论中关键概念的简要解释。*

### 混合专家模型 (Mixture of Experts, MoE)
一种神经网络架构，模型由许多“专家”子网络组成，一个“路由器”为每个输入词元决定使用哪些专家。

### 路由器 (Router)
MoE模型中的组件，它接收一个词元的表示，并输出一个在可用专家上的概率分布。

### 自适应K路由 (Adaptive-K Routing)
一种动态路由策略，其中每个词元选择的专家数量（K）不是固定的，而是基于路由器对该词元的置信度（熵）动态决定的。

### 熵（在本语境中）
衡量路由器概率分布不确定性或分散程度的指标。**低熵**表示路由器信心足（某个专家概率很高）。**高熵**表示路由器不确定（概率分布更平均）。

### 负载均衡 (Load Balancing)
在MoE训练中，确保所有专家都能获得大致等量的训练数据，防止某些专家未被充分利用的挑战。

---
*此术语表将随着项目深入而持续完善。*
