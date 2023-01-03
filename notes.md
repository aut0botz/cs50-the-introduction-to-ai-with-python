##  Search

### Search Problems

#### agent

![image-20221130145008567](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221130145008567.png)

#### state

![image-20221130145018091](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221130145018091.png)

#### initial state

![image-20221130145103478](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221130145103478.png)

#### actions

![image-20221130145138092](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221130145138092.png)

![image-20221130145330409](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221130145330409.png)

#### transition model

![image-20221130145619175](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221130145619175.png)

![image-20221130145624260](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221130145624260.png)

#### state space

![image-20221130145656789](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221130145656789.png)

#### goal test

![image-20221130150026808](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221130150026808.png)

#### path cost

![image-20221130150040593](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221130150040593.png)

#### search problems

![image-20221130150122115](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221130150122115.png)

#### solution

![image-20221130150139740](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221130150139740.png)

#### optimal solution

![image-20221130150150019](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221130150150019.png)

#### node

![image-20221130150211130](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221130150211130.png)

#### approach

![image-20221130150221760](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221130150221760.png)

### uninformed search

![image-20221130150447574](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221130150447574.png)

#### depth-first search

![image-20221130150330731](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221130150330731.png)

#### breadth-first search

![image-20221130150348917](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221130150348917.png)

### informed search

![image-20221130150512897](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221130150512897.png)

#### greedy best-first search

![image-20221130150532490](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221130150532490.png)

#### A* search

![image-20221130150705909](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221130150705909.png)

![image-20221130150756581](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221130150756581.png)

**注意：这里的高估可以这样来理解，这个启发式函数要么认为该状态到达目标的距离是低于真实距离的，或者等于，但是不能够认为该点到目标的距离是大于真实距离的。如下图，右上角有两个距离为2的，左边那个是低估了该点到目标的距离，右边那个则是刚好等于该点到目标的距离。**

![image-20221130154401555](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221130154401555.png)

### adversarial search

#### Minmax

![image-20221130155632823](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221130155632823.png)

![image-20221130155535230](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221130155535230.png)

##### game

![image-20221130155642606](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221130155642606.png)

##### initial state

![image-20221130155651550](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221130155651550.png)

##### player(s)

![image-20221130155720089](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221130155720089.png)

##### action(s)

![image-20221130155856074](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221130155856074.png)

##### result(s,a)

![image-20221130155916512](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221130155916512.png)

##### terminal(s)

![image-20221130155926292](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221130155926292.png)

##### utility(s)

![image-20221130155942439](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221130155942439.png)

#### Minmax_algorithm

![image-20221130160203669](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221130160203669.png)

![image-20221130160209261](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221130160209261.png)

![image-20221130160214366](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221130160214366.png)

##### Optimizations

###### Alpha-Beta Pruning

![image-20221130165509131](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221130165509131.png)

但是，当需要处理的数据很多的时候，这种方法也是不行的，于是出现了Depth-Limited Minmax。

###### Depth-Limited Minmax

​	Depth-limited Minmax 在停止之前只考虑预先定义的移动次数，而不会到达终止状态。 然而，这不允许为每个动作获得精确的值，因为假设的游戏还没有结束。 为了解决这个问题，深度受限的 Minimax 依赖于一个evaluation function，该函数从给定状态估计游戏的预期效用，或者换句话说，为状态赋值。 例如，在国际象棋游戏中，效用函数会将棋盘的当前配置作为输入，尝试评估其预期效用（基于每个玩家拥有的棋子及其在棋盘上的位置），然后返回正或 一个负值，表示棋盘对一个玩家相对于另一个玩家的有利程度。 这些值可以用来决定正确的动作，评估函数越好，依赖于它的 Minimax 算法就越好。

![image-20221130170423265](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221130170423265.png)

## Knowledge

Humans reason based on existing knowledge and draw conclusions. The concept of representing knowledge and drawing conclusions from it is also used in AI, and in this lecture we will explore how we can achieve this behavior.

### Knowledge-Based Agents

![image-20221201202952911](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221201202952911.png)

![image-20221201203323168](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221201203323168.png)

### sentence

![image-20221201203010176](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221201203010176.png)

A sentence is an assertion about the world in a knowledge representation language. A sentence is how AI stores knowledge and uses it to infer new information.

### Propositional Logic

Propositional logic is based on propositions, statements about the world that can be either true or false.

#### Propositional Symbols

![image-20221201203103781](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221201203103781.png)

#### Logic Connectives

![image-20221201203116443](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221201203116443.png)

Logical connectives are logical symbols that connect propositional symbols in order to reason in a more complex way about the world.

##### Not (¬)

![image-20221201203136511](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221201203136511.png)

##### And (∧)

![image-20221201203147187](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221201203147187.png)

##### Or (∨)

![image-20221201203209169](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221201203209169.png)

###### inclusive Or

An inclusive Or is true if any of P, Q, or P ∧ Q is true.

###### exclusive Or

In an exclusive Or, P ∨ Q is false if P ∧ Q is true. That is, an exclusive Or requires only one of its arguments to be true and not both.

the exclusive Or is often shortened to XOR and a common symbol for it is ⊕.

##### Implication (→)

![image-20221201203222321](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221201203222321.png)

##### Biconditional (↔)

![image-20221201203232068](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221201203232068.png)

#### Model

![image-20221201203255028](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221201203255028.png)

The model is an assignment of a truth value to every proposition. To reiterate, propositions are statements about the world that can be either true or false. However, knowledge about the world is represented in the truth values of these propositions. The model is the truth-value assignment that provides information about the world.

#### knowledge base

![image-20221201203408324](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221201203408324.png)

The knowledge base is a set of sentences known by a knowledge-based agent. This is knowledge that the AI is provided about the world in the form of propositional logic sentences that can be used to make additional inferences about the world.

#### Entailment

![image-20221201203423882](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221201203423882.png)

Entailment is different from implication. Implication is a logical connective between two propositions. Entailment, on the other hand, is a relation that means that if all the information in α is true, then all the information in β is true.

### inference

![image-20221201203445883](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221201203445883.png)

#### Inference Algorithms

![image-20221201205909642](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221201205909642.png)

##### Model Checking

![image-20221201203702919](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221201203702919.png)

![image-20221201210059730](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221201210059730.png)

Looking at this table, there is only one model where our knowledge base is true. In this model, we see that R is also true. By our definition of entailment, if R is true in all models where the KB is true, then KB ⊨ R.

#### Inference Rules

Model Checking is not an efficient algorithm because it has to consider every possible model before giving the answer (a reminder: a query R is true if under all the models (truth assignments) where the KB is true, R is true as well). Inference rules allow us to generate new information based on existing knowledge without considering every possible model.

Inference rules are usually represented using a horizontal bar that separates the top part, the premise, from the bottom part, the conclusion. The premise is whatever knowledge we have, and the conclusion is what knowledge can be generated based on the premise.

##### Modus Ponens

![image-20221201204011017](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221201204011017.png)

##### And Elimination

![image-20221201204029105](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221201204029105.png)

##### Double Negation Elimination

![image-20221201204046344](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221201204046344.png)

##### Implication Elimination

![image-20221201204120611](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221201204120611.png)

##### Biconditional Elimination

![image-20221201204133282](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221201204133282.png)

##### De morgan's Law

![image-20221201204147480](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221201204147480.png)

![image-20221201204158864](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221201204158864.png)

##### Distributive Property

![image-20221201204216795](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221201204216795.png)

![image-20221201204221395](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221201204221395.png)

##### Resolution

![image-20221202094758574](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221202094758574.png)

![image-20221202094806617](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221202094806617.png)

![image-20221202094812376](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221202094812376.png)

![image-20221202094818292](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221202094818292.png)

#### clause

![image-20221202094831766](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221202094831766.png)

- A disjunction consists of propositions that are connected with an Or logical connective (P ∨ Q ∨ R).
- A conjunction consists of propositions that are connected with an And logical connective (P ∧ Q ∧ R).

#### conjunctive normal form

![image-20221202094852807](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221202094852807.png)

##### Conversion to CNF

![image-20221202100246102](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221202100246102.png)

#### Inference by Resolution

![image-20221202100842189](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221202100842189.png)

![image-20221202100848329](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221202100848329.png)

### First-Order Logic

![image-20221202101909052](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221202101909052.png)

First order logic is another type of logic that allows us to express more complex ideas more succinctly than propositional logic. First order logic uses two types of symbols: Constant Symbols and Predicate Symbols. Constant symbols represent objects, while predicate symbols are like relations or functions that take an argument and return a true or false value.

![image-20221202101916117](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221202101916117.png)

Quantification is a tool that can be used in first order logic to represent sentences without using a specific constant symbol.

#### Universal Quantification

![image-20221202101951248](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221202101951248.png)

#### Existential Quantification

![image-20221202102007619](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221202102007619.png)

Existential and universal quantification can be used in the same sentence. For example, the sentence ∀x. Person(x) → (∃y. House(y) ∧ BelongsTo(x, y)) expresses the idea that if x is a person, then there is at least one house, y, to which this person belongs. In other words, this sentence means that every person belongs to a house.

![image-20221202102014961](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221202102014961.png)

## Uncertainty

Last lecture, we discussed how AI can represent and derive new knowledge. However, often, in reality, the AI has only partial knowledge of the world, leaving space for uncertainty. Still, we would like our AI to make the best possible decision in these situations.

### Probability

Uncertainty can be represented as a number of events and the likelihood, or probability, of each of them happening.

#### Possible worlds

Every possible situation can be thought of as a world, represented by the lowercase Greek letter omega ω.

To represent the probability of a certain world, we write P(ω).

#### Axioms in Probability

![image-20221204150253138](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221204150253138.png)

- Zero is an impossible event.
- One is an event that is certain to happen.
- In general, the higher the value, the more likely the event is to happen.

![image-20221204150407838](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221204150407838.png)

#### unconditional probability

![image-20221204150539595](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221204150539595.png)

#### conditional probability

![image-20221204150652922](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221204150652922.png)

Conditional probability is expressed using the following notation: P(a | b), meaning “the probability of event a occurring given that we know event b to have occurred,” or, more succinctly, “the probability of a given b.”

Mathematically, to compute the conditional probability of a given b, we use the following formula:

![image-20221204151015002](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221204151015002.png)

The following are algebraically equivalent forms to the formula above:

![image-20221204151151067](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221204151151067.png)

#### joint probability

Joint probability is the likelihood of multiple events all occurring.

Using joint probabilities, we can deduce conditional probability.

### random variable

![image-20221204151301881](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221204151301881.png)

A random variable is a variable in probability theory with a domain of possible values that it can take on.

Often, we are interested in the probability with which each value occurs. We represent this using a probability distribution.

A probability distribution can be represented more succinctly as a vector.

#### independence

![image-20221204151530244](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221204151530244.png)

Independence can be defined mathematically: events a and b are independent if and only if the probability of a and b is equal to the probability of a times the probability of b: P(a ∧ b) = P(a)P(b):

![image-20221204152020797](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221204152020797.png)

### Bays' Rule

![image-20221204152119383](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221204152119383.png)

Bayes’ rule is commonly used in probability theory to compute conditional probability.

Knowing P(a | b), in addition to P(a) and P(b), allows us to calculate P(b | a).

This is helpful, because knowing the conditional probability of a visible effect given an unknown cause, P(visible effect | unknown cause), allows us to calculate the probability of the unknown cause given the visible effect, P(unknown cause | visible effect).

For example, we can learn P(medical test results | disease) through medical trials, where we test people with the disease and see how often the test picks up on that. Knowing this, we can calculate P(disease | medical test results), which is valuable diagnostic information.

### Probability Rules

#### Negation

![image-20221204154154408](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221204154154408.png)

#### Inclusion-Exclusion

![image-20221204154349676](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221204154349676.png)

#### Marginalization

![image-20221204154416969](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221204154416969.png)

Marginalization can be expressed for random variables the following way:

![image-20221204154539099](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221204154539099.png)

#### Conditioning

![image-20221204154626157](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221204154626157.png)

Conditioning can also be expressed for random variables the following way:

![image-20221204154838118](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221204154838118.png)

### Bayesian Network

#### introduction

![image-20221204154918565](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221204154918565.png)

Bayesian networks have the following properties:

![image-20221204154953422](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221204154953422.png)

#### example

Let’s consider an example of a Bayesian network that involves variables that affect whether we get to our appointment on time.

![image-20221204155442467](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221204155442467.png)

For example, if we want to find the probability of missing the meeting when the train was delayed on a day with no maintenance and light rain, or P(light, no, delayed, miss), we will compute the following: P(light)P(no | light)P(delayed | light, no)P(miss | delayed). The value of each of the individual probabilities can be found in the probability distributions above, and then these values are multiplied to produce P(no, light, delayed, miss).

#### inference

At the last lecture, we looked at inference through entailment. This means that we could definitively conclude new information based on the information that we already had. We can also infer new information based on probabilities. While this does not allow us to know new information for certain, it allows us to figure out the probability distributions for some values. Inference has multiple properties:

![image-20221204161011567](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221204161011567.png)

example:

![image-20221204161550497](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221204161550497.png)

#### inference by Enumeration

Inference by enumeration is a process of finding the probability distribution of variable X given observed evidence e and some hidden variables Y.

![image-20221204161638956](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221204161638956.png)

To explain the equation in words, it is saying that the probability distribution of X given e is equal to a normalized probability distribution of X and e. To get to this distribution, we sum the normalized probability of X, e, and y, where y takes each time a different value of the hidden variables Y.

This way of computing probability is inefficient, especially when there are many variables in the model. A different way to go about this would be abandoning exact inference in favor of approximate inference. Doing this, we lose some precision in the generated probabilities, but often this imprecision is negligible. Instead, we gain a scalable method of calculating probabilities.

### Sampling

Sampling is one technique of approximate inference. In sampling, each variable is sampled for a value according to its probability distribution.

Here is an example from lecture: if we start with sampling the Rain variable, the value none will be generated with probability of 0.7, the value light will be generated with probability of 0.2, and the value heavy will be generated with probability of 0.1. Suppose that the sampled value we get is none. When we get to the Maintenance variable, we sample it, too, but only from the probability distribution where Rain is equal to none, because this is an already sampled result. We will continue to do so through all the nodes. Now we have one sample, and repeating this process multiple times generates a distribution. 

Now, if we want to answer a question, such as what is P(Train = on time), we can count the number of samples where the variable Train has the value on time, and divide the result by the total number of samples. This way, we have just generated an approximate probability for P(Train = on time). 

We can also answer questions that involve conditional probability, such as P(Rain = light | Train = on time). In this case, we ignore all samples where the value of Train is not on time, and then proceed as before. We count how many samples have the variable Rain = light among those samples that have Train = on time, and then divide by the total number of samples where Train = on time.

#### likelihood weighting

In the sampling example above, we discarded the samples that did not match the evidence that we had. This is inefficient. One way to get around this is with likelihood weighting, using the following steps:

![image-20221204164259762](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221204164259762.png)

For example, if we have the observation that the train was on time, we will start sampling as before. We sample a value of Rain given its probability distribution, then Maintenance, but when we get to Train - we always give it the observed value, in our case, on time. Then we proceed and sample Appointment based on its probability distribution given Train = on time. Now that this sample exists, we weight it by the conditional probability of the observed variable given its sampled parents. That is, if we sampled Rain and got light, and then we sampled Maintenance and got yes, then we will weight this sample by P(Train = on time | light, yes).

### Markov Models

So far, we have looked at questions of probability given some information that we observed. In this kind of paradigm, the dimension of time is not represented in any way. However, many tasks do rely on the dimension of time, such as prediction. To represent the variable of time we will create a new variable, X, and change it based on the event of interest, such that $x_t$ is the current event, $x_{t+1}$ is the next event, and so on. To be able to predict events in the future, we will use Markov Models.

#### Markov assumption

![image-20221204164911207](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221204164911207.png)

The Markov assumption is an assumption that the current state depends on only a finite fixed number of previous states. This is important to us.

Think of the task of predicting weather. In theory, we could use all the data from the past year to predict tomorrow’s weather. However, it is infeasible, both because of the computational power this would require and because there is probably no information about the conditional probability of tomorrow’s weather based on the weather 365 days ago. Using the Markov assumption, we restrict our previous states (e.g. how many previous days we are going to consider when predicting tomorrow’s weather), thereby making the task manageable. This means that we might get a more rough approximation of the probabilities of interest, but this is often good enough for our needs. 

Moreover, we can use a Markov model based on the information of the one last event (e.g. predicting tomorrow’s weather based on today’s weather).

#### Markov chain

![image-20221204164930517](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221204164930517.png)

A Markov chain is a sequence of random variables where the distribution of each variable follows the Markov assumption. That is, each event in the chain occurs based on the probability of the event before it.

### Hidden Markov Models

![image-20221204165030764](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221204165030764.png)

A hidden Markov model is a type of a Markov model for a system with hidden states that generate some observed event. This means that sometimes, the AI has some measurement of the world but no access to the precise state of the world. In these cases, the state of the world is called **the hidden state** and whatever data the AI has access to are **the observations**. 

Here are a few examples for this:

- For a robot exploring uncharted territory, the hidden state is its position, and the observation is the data recorded by the robot’s sensors.
- In speech recognition, the hidden state is the words that were spoken, and the observation is the audio waveforms. 
- When measuring user engagement on websites, the hidden state is how engaged the user is, and the observation is the website or app analytics.

For our discussion, we will use the following example. Our AI wants to infer the weather (the hidden state), but it only has access to an indoor camera that records how many people brought umbrellas with them. Here is our **sensor model** (also called **emission model**) that represents these probabilities:

![image-20221204170459502](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221204170459502.png)

In this model, if it is sunny, it is most probable that people will not bring umbrellas to the building. If it is rainy, then it is very likely that people bring umbrellas to the building. By using the observation of whether people brought an umbrella or not, we can predict with reasonable likelihood what the weather is outside.

#### sensor Markov assumption

![image-20221204165109763](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221204165109763.png)

For example, for our models, we assume that whether people bring umbrellas to the office depends only on the weather. This is not necessarily reflective of the complete truth, because, for example, more conscientious, rain-averse people might take an umbrella with them everywhere even when it is sunny, and if we knew everyone’s personalities it would add more data to the model. However, the sensor Markov assumption ignores these data, assuming that only the hidden state affects the observation. 

A hidden Markov model can be represented in a Markov chain with two layers. The top layer, variable X, stands for the hidden state. The bottom layer, variable E, stands for the evidence, the observations that we have.

![image-20221204171136189](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221204171136189.png)

Based on hidden Markov models, multiple tasks can be achieved:

- Filtering: given observations from start until now, calculate the probability distribution for the current state. For example, given information on when people bring umbrellas form the start of time until today, we generate a probability distribution for whether it is raining today or not. 
- Prediction: given observations from start until now, calculate the probability distribution for a future state. 
- Smoothing: given observations from start until now, calculate the probability distribution for a past state. For example, calculating the probability of rain yesterday given that people brought umbrellas today. 
- Most likely explanation: given observations from start until now, calculate most likely sequence of events.

## Optimization

![image-20221208153817516](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221208153817516.png)

### local search

![image-20221208153843578](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221208153843578.png)

- An **Objective Function** is a function that we use to maximize the value of the solution.
- A **Cost Function** is a function that we use to minimize the cost of the solution
- A **Current State** is the state that is currently being considered by the function.
- A **Neighbor State** is a state that the current state can transition to.

#### Hill Climbing

##### algorithm

Hill climbing is one type of a local search algorithm. In this algorithm, the neighbor states are compared to the current state, and if any of them is better, we change the current node from the current state to that neighbor state. What qualifies as better is defined by whether we use an objective function, preferring a higher value, or a decreasing function, preferring a lower value.

![image-20221208154342108](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221208154342108.png)

##### Local and Global Minima and Maxima

- A **local maximum** (plural: maxima) is a state that has a higher value than its neighboring states.
- As opposed to that, a **global maximum** is a state that has the highest value of all states in the state-space.
- A **local minimum** (plural: minima) is a state that has a lower value than its neighboring states.
- As opposed to that, a **global minimum** is a state that has the lowest value of all states in the state-space.
- Special types of local maxima and minima include the **flat local maximum/minimum**, where multiple states of equal value are adjacent, forming a plateau whose neighbors have a worse value, and the **shoulder**, where multiple states of equal value are adjacent and the neighbors of the plateau can be both better and worse.

##### Hill Climbing Variants

What all variations of the algorithm have in common is that, no matter the strategy, each one still has the potential of ending up in local minima and maxima and no means to continue optimizing.

![image-20221208155057051](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221208155057051.png)

- **Steepest-ascent**: choose the highest-valued neighbor. This is the standard variation that we discussed above.
- **Stochastic**: choose randomly from higher-valued neighbors. Doing this, we choose to go to any direction that improves over our value. This makes sense if, for example, the highest-valued neighbor leads to a local maximum while another neighbor leads to a global maximum.
- **First-choice**: choose the first higher-valued neighbor.
- **Random-restart**: conduct hill climbing multiple times. Each time, start from a random state. Compare the maxima from every trial, and choose the highest amongst those.
- **Local Beam Search**: chooses the k highest-valued neighbors. This is unlike most local search algorithms in that it uses multiple nodes for the search, and not just one.

### Simulated Annealing

Although we have seen variants that can improve hill climbing, they all share the same fault: once the algorithm reaches a local maximum, it stops running. Simulated annealing allows the algorithm to “dislodge” itself if it gets stuck in a local maximum.

![image-20221208155839126](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221208155839126.png)

#### algorithm

![image-20221208160102861](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221208160102861.png)

#### Traveling Salesman Problem

![image-20221208160233811](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221208160233811.png)

In the traveling salesman problem, the task is to connect all points while choosing the shortest possible distance. In this case, a neighbor state might be seen as a state where two arrows swap places.

### Linear Programming

Linear programming is a family of problems that optimize a linear equation (an equation of the form y = ax₁ + bx₂ + …).

![image-20221208161319381](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221208161319381.png)

- A cost function that we want to minimize: $c_1x_1+c_2x_2+...+c_nx_n$. Here, each x₋ is a variable and it is associated with some cost c₋.
- A constraint that’s represented as a sum of variables that is either less than or equal to a value ($a_1x_1+a_2x_2+...+a_nx_n ≤ b$) or precisely equal to this value ($a_1x_1+a_2x_2+...+a_nx_n =b$). In this case, x- is a variable, and a- is some resource associated with it, and b is how much resources we can dedicate to this problem.
- Individual bounds on variables (for example, that a variable can’t be negative) of the form $l_i ≤ x_i ≤u_i$.

### Constraint Satisfaction

Constraint Satisfaction problems are a class of problems where variables need to be assigned values while satisfying some conditions.

#### Constraint Satisfaction Problem

![image-20221208162044889](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221208162044889.png)

A few more terms worth knowing about constraint satisfaction problems:

- A **Hard Constraint** is a constraint that must be satisfied in a correct solution.
- A **Soft Constraint** is a constraint that expresses which solution is preferred over others.
- A **Unary Constraint** is a constraint that involves only one variable.
- A **Binary Constraint** is a constraint that involves two variables.

#### Node Consistency

![image-20221208163054319](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221208163054319.png)

#### Arc Consistency

![image-20221208163110634](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221208163110634.png)

![image-20221208163120144](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221208163120144.png)

Let’s look at an algorithm in pseudocode that makes a variable arc-consistent with respect to some other variable (note that csp stands for “constraint satisfaction problem”):

![image-20221208163516849](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221208163516849.png)

This algorithm starts with tracking whether any change was made to X’s domain, using the variable revised. This will be useful in the next algorithm we examine. Then, the code repeats for every value in X’s domain and sees if Y has a value that satisfies the constraints. If yes, then do nothing, if not, remove this value from X’s domain.

Often we are interested in making the whole problem arc-consistent and not just one variable with respect to another. In this case, we will use an algorithm called AC-3, which uses Revise:

![image-20221208163625860](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221208163625860.png)

This algorithm adds all the arcs in the problem to a queue. Each time it considers an arc, it removes it from the queue. Then, it runs the Revise algorithm to see if this arc is consistent. If changes were made to make it consistent, further actions are needed. If the resulting domain of X is empty, it means that this constraint satisfaction problem is unsolvable (since there are no values that X can take that will allow Y to take any value given the constraints). If the problem is not deemed unsolvable in the previous step, then, since X’s domain was changed, we need to see if all the arcs associated with X are still consistent. That is, we take all of X’s neighbors except Y, and we add the arcs between them and X to the queue. However, if the Revise algorithm returns false, meaning that the domain wasn’t changed, we simply continue considering the other arcs.

#### CSPs as Search Problems

![image-20221208163730096](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221208163730096.png)

However, going about a constraint satisfaction problem naively, as a regular search problem, is massively inefficient. Instead, we can make use of the structure of a constraint satisfaction problem to solve it more efficiently.

### Backtracking Search

#### algorithm

Backtracking search is a type of a search algorithm that takes into account the structure of a constraint satisfaction search problem. In general, it is a recursive function that attempts to continue assigning values as long as they satisfy the constraints. If constraints are violated, it tries a different assignment.

![image-20221208164357956](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221208164357956.png)

In words, this algorithm starts with returning the current assignment if it is complete. This means that, if the algorithm is done, it will not perform any of the additional actions. Instead, it will just return the completed assignment. If the assignment is not complete, the algorithm selects any of the variables that do not have an assignment yet. Then, the algorithm tries to assign a value to the variable, and runs the Backtrack algorithm again on the resulting assignment (recursion). Then, it checks the resulting value. If it is not failure, it means that the assignment worked out, and it should return this assignment. If the resulting value is failure, then the latest assignment is removed, and a new possible value is attempted, repeating the same process. If all possible values in the domain returned failure, this means that we need to backtrack. That is, that the problem is with some previous assignment. If this happens with the variable we start with, then it means that no solution satisfies the constraints.

#### inference

Although backtracking search is more efficient than simple search, it still takes a lot of computational power. Enforcing arc consistency, on the other hand, is less resource intensive. By interleaving backtracking search with inference (enforcing arc consistency), we can get at a more efficient algorithm. This algorithm is called the **Maintaining Arc-Consistency algorithm**.

This algorithm will enforce arc-consistency after every new assignment of the backtracking search. Specifically, after we make a new assignment to X, we will call the AC-3 algorithm and start it with a queue of all arcs (Y,X) where Y is a neighbor of X (and not a queue of all arcs in the problem).

![image-20221208164940591](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221208164940591.png)

The Inference function runs the AC-3 algorithm as described. Its output is all the inferences that can be made through enforcing arc-consistency. **Literally, these are the new assignments that can be deduced from the previous assignments and the structure of the constrain satisfaction problem.**

There are additional ways to make the algorithm more efficient. So far, we selected an unassigned variable randomly. However, some choices are more likely to bring to a solution faster than others. This requires the use of heuristics. A heuristic is a rule of thumb, meaning that, more often than not, it will bring to a better result than following a naive approach, but it is not guaranteed to do so.

#### SELECT-UNASSIGNED-VAR

![image-20221208165526378](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221208165526378.png)

##### Minimum Remaining Values (MRV)

**Minimum Remaining Values (MRV)** is one such heuristic. The idea here is that if a variable’s domain was constricted by inference, and now it has only one value left (or even if it’s two values), then by making this assignment we will reduce the number of backtracks we might need to do later. That is, we will have to make this assignment sooner or later, since it’s inferred from enforcing arc-consistency. If this assignment brings to failure, it is better to find out about it as soon as possible and not backtrack later.

##### Degree heuristic

The **Degree heuristic** relies on the degrees of variables, where a degree is how many arcs connect a variable to other variables. By choosing the variable with the highest degree, with one assignment, we constrain multiple other variables, speeding the algorithm’s process.

#### DOMAIN-VALUES

Another way to make the algorithm more efficient is employing yet another heuristic when we select a value from the domain of a variable.

![image-20221208165743135](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221208165743135.png)

##### Least Constraining Values heuristic

Here, we would like to use the Least Constraining Values heuristic, where we select the value that will constrain the least other variables. The idea here is that, while in the degree heuristic we wanted to use the variable that is more likely to constrain other variables, here we want this variable to place the least constraints on other variables. **That is, we want to locate what could be the largest potential source of trouble (the variable with the highest degree), and then render it the least troublesome that we can (assign the least constraining value to it).**

## Machine Learning

### supervised learning

![image-20221209144726749](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221209144726749.png)

Supervised learning is a task where a computer learns a function that maps inputs to outputs based on a dataset of input-output pairs.

#### classification

![image-20221209144803330](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221209144803330.png)

##### nearest-neighbor classification

![image-20221209145650647](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221209145650647.png)

Also can be called as 1-nearest-neighbor classification.

###### k-nearest-neighbor classification

![image-20221209145811137](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221209145811137.png)

A drawback of the k-nearest-neighbors classification is that, using a naive approach, the algorithm will have to measure the distance of every single point to the point in question, which is computationally expensive. This can be sped up by using data structures that enable finding neighbors more quickly or by pruning irrelevant observation.

##### perceptron learning 

Another way of going about a classification problem, as opposed to the nearest-neighbor strategy, is looking at the data as a whole and trying to create a decision boundary. In two-dimensional data, we can draw a line between the two types of observations. Every additional data point will be classified based on the side of the line on which it is plotted.

The drawback to this approach is that data are messy, and it is rare that one can draw a line and neatly divide the classes into two observations without any mistakes. Often, we will compromise, drawing a boundary that separates the observations correctly more often than not, but still occasionally mis-classifies them.

![image-20221209150918334](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221209150918334.png)

Since the goal of the algorithm is to find the best weight vector, when the algorithm encounters new data it updates the current weights. It does so using the **perceptron learning rule**:

![image-20221209151017776](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221209151017776.png)

The higher α, the stronger the influence each new event has on the weight.

The **result of this process** is a threshold function that switches from 0 to 1 once the estimated value crosses some threshold.

![image-20221209151611375](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221209151611375.png)

The problem with this type of function is that it is unable to express uncertainty, since it can only be equal to 0 or to 1. It employs a hard threshold. A way to go around this is by using a logistic function, which employs a soft threshold. A logistic function can yield a real number between 0 and 1, which will express confidence in the estimate. The closer the value to 1, the more likely it is to rain.

![image-20221209151623211](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221209151623211.png)

##### support vector machine

In addition to nearest-neighbor and linear regression, another approach to classification is the Support Vector Machine. This approach uses an additional vector (support vector) near the decision boundary to make the best decision when separating the data. Consider the example below.

![image-20221209151942047](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221209151942047.png)

All the decision boundaries work in that they separate the data without any mistakes. However, are they equally as good? The two leftmost decision boundaries are very close to some of the observations. This means that a new data point that differs only slightly from one group can be wrongly classified as the other. As opposed to that, the rightmost decision boundary keeps the most distance from each of the groups, thus giving the most leeway for variation within it. This type of boundary, which is as far as possible from the two groups it separates, is called the Maximum Margin Separator.

Another benefit of support vector machines is that they can represent decision boundaries with more than two dimensions, as well as **non-linear decision boundaries**.

#### regression

![image-20221209152109148](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221209152109148.png)

Regression is a supervised learning task of a function that maps an input point to a continuous value, some real number. This differs from classification in that classification problems map an input to discrete values (Rain or No Rain).

### loss function

![image-20221209152332915](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221209152332915.png)

Loss functions are a way to quantify the utility lost by any of the decision rules above. The less accurate the prediction, the larger the loss.

#### 0-1 loss function

For classification problems, we can use a 0-1 Loss Function.

![image-20221209152414231](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221209152414231.png)

#### $L_1$ loss function

L₁ and L₂ loss functions can be used when predicting a continuous value.

In this case, we are interested in quantifying for each prediction how much it differed from the observed value. We do this by taking either the absolute value or the squared value of the observed value minus the predicted value (i.e. how far the prediction was from the observed value).

![image-20221209152519618](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221209152519618.png)

#### $L_2$ loss function

![image-20221209152535335](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221209152535335.png)

One can choose the loss function that serves their goals best. L₂ penalizes outliers more harshly than L₁ because it squares the the difference.

### overfitting

![image-20221209152721977](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221209152721977.png)

Overfitting is when a model fits the training data so well that it fails to generalize to other data sets. In this sense, loss functions are a double edged sword.

### regularization

![image-20221209152938045](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221209152938045.png)

Regularization is the process of penalizing hypotheses that are more complex to favor simpler, more general hypotheses. We use regularization to avoid overfitting.

In regularization, we estimate the cost of the hypothesis function h by adding up its loss and a measure of its complexity.

Lambda (λ) is a constant that we can use to modulate how strongly to penalize for complexity in our cost function. The higher λ is, the more costly complexity is.

#### holdout cross-validation

![image-20221209153137409](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221209153137409.png)

One way to test whether we overfitted the model is with Holdout Cross Validation. In this technique, we split all the data in two: a training set and a test set. We run the learning algorithm on the training set, and then see how well it predicts the data in the test set. The idea here is that by testing on data that were not used in training, we can measure how well the learning generalizes.

The downside of holdout cross validation is that **we don’t get to train the model on half the data, since it is used for evaluation purposes**.

#### k-fold cross-validation

![image-20221209153408674](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221209153408674.png)

In this process, we divide the data into k sets. We run the training k times, each time leaving out one dataset and using it as a test set. We end up with k different evaluations of our model, which we can average and get an estimate of how our model generalizes without losing any data.

### reinforcement learning

![image-20221209153757583](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221209153757583.png)

Reinforcement learning is another approach to machine learning, where after each action, the agent gets feedback in the form of reward or punishment (a positive or a negative numerical value).

![image-20221209153807361](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221209153807361.png)

The learning process starts by the environment providing a state to the agent. Then, the agent performs an action on the state. Based on this action, the environment will return a state and a reward to the agent, where the reward can be positive, making the behavior more likely in the future, or negative (i.e. punishment), making the behavior less likely in the future.

#### Markov Decision Process

![image-20221209154153427](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221209154153427.png)

Reinforcement learning can be viewed as a Markov decision process, having the following properties:

![image-20221209154205692](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221209154205692.png)

The algorithm can be probabilistic, choosing to take different actions in different states based on some probability that’s being increased or decreased based on reward.

#### Q-learning

Q-Learning is one model of reinforcement learning, where a function Q(s, a) outputs an estimate of the value of taking action a in state s.

![image-20221209154807965](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221209154807965.png)

This gives us an algorithm that is capable of improving upon its past knowledge without starting from scratch.

![image-20221209155003727](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221209155003727.png)

The updated value of Q(s, a) is equal to the previous value of Q(s, a) in addition to some updating value. This value is determined as the difference between the new value and the old value, multiplied by α, a learning coefficient. 

- When α = 1 the new estimate simply overwrites the old one. 
- When α = 0, the estimated value is never updated. 

By raising and lowering α, we can determine how fast previous knowledge is being updated by new estimates.

The new value estimate can be expressed as a sum of the reward (r) and the future reward estimate. To get the future reward estimate, we consider the new state that we got after taking the last action, and add the estimate of the action in this new state that will bring to the highest reward. This way, we estimate the utility of making action a in state s not only by the reward it received, but also by the expected utility of the next step. The value of the future reward estimate can sometimes appear with a coefficient gamma that controls how much future rewards are valued. We end up with the following equation:

![image-20221209155106563](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221209155106563.png)

A Greedy Decision-Making algorithm completely discounts the future estimated rewards, instead always choosing the action a in current state s that has the highest Q(s, a).

This brings us to discuss the **Explore vs. Exploit** tradeoff:

- A greedy algorithm always exploits, taking the actions that are already established to bring to good outcomes. However, it will always follow the same path to the solution, never finding a better path.
- Exploration, on the other hand, means that the algorithm may use a previously unexplored route on its way to the target, allowing it to discover more efficient solutions along the way.

To implement the concept of exploration and exploitation, we can use the **ε (epsilon) greedy algorithm**. In this type of algorithm, we set ε equal to how often we want to move randomly. With probability 1-ε, the algorithm chooses the best move (exploitation). With probability ε, the algorithm chooses a random move (exploration).

Another way to train a reinforcement learning model is to give feedback not upon every move, but upon the end of the whole process.

### unsupervised learning

![image-20221210110132305](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221210110132305.png)

In all the cases we saw before, as in supervised learning, we had data with labels that the algorithm could learn from. In unsupervised learning, only the input data is present and the AI learns patterns in these data.

#### clustering

![image-20221210110232800](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221210110232800.png)

##### k-means clustering

![image-20221210110316998](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221210110316998.png)

k-means Clustering is an algorithm to perform a clustering task. It maps all data points in a space, and then randomly places k cluster centers in the space. Each cluster center is simply a point in the space. Then, each cluster gets assigned all the points that are closest to its center than to any other center. Then, in an iterative process, the cluster center moves to the middle of all these points, and then points are reassigned again to the clusters whose centers are now closest to them. When, after repeating the process, each point remains in the same cluster it was before, we have reached an equilibrium and the algorithm is over, leaving us with points divided between clusters.

## Neural Networks

![image-20221215090120429](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221215090120429.png)

An **Artificial Neural Network** is a mathematical model for learning inspired by biological neural networks.

![image-20221215090144531](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221215090144531.png)

When implemented in AI, the parallel of each neuron is a **unit** that’s connected to other units.

### Activation Function

#### step function

![image-20221215090207128](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221215090207128.png)

#### logistic sigmoid

![image-20221215090219988](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221215090219988.png)

#### rectified linear unit (ReLU)

![image-20221215090238939](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221215090238939.png)

### Neural Network Structure

![image-20221215090843221](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221215090843221.png)

### Gradient Descent

Gradient descent is an algorithm for minimizing loss when training neural networks.

![image-20221215091137269](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221215091137269.png)

The problem with this kind of algorithm is that it requires to calculate the gradient based on all data points, which is computationally costly.

There are a multiple ways to minimize this cost. For example, in **Stochastic Gradient Descent**, the gradient is calculated based on one point chosen at random. This kind of gradient can be quite inaccurate, leading to the **Mini-Batch Gradient Descent** algorithm, which computes the gradient based on on a few points selected at random, thus finding a compromise between computation cost and accuracy. As often is the case, none of these solutions is perfect, and different solutions might be employed in different situations.

This can be done with any number of inputs and outputs, where each input is connected to each output, and where the outputs represent decisions that we can make. Note that in this kind of neural networks the outputs are not connected. **This means that each output and its associated weights from all the inputs can be be seen as an individual neural network and thus can be trained separately from the rest of the outputs.**

So far, our neural networks relied on **perceptron** output units. These are units that are only capable of learning a linear decision boundary, using a straight line to separate data.

### Multilayer Neural Network

A multilayer neural network is an artificial neural network with an input layer, an output layer, and **at least one hidden layer**. 

![image-20221215092214134](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221215092214134.png)

Through hidden layers, it is possible to model non-linear data.

### Backpropagation

Backpropagation is the main algorithm used for training neural networks with hidden layers.

![image-20221215092302070](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221215092302070.png)

This can be extended to any number of hidden layers, creating **deep neural networks**, which are neural networks that have more than one hidden layer.

### Overfitting

Overfitting is the danger of modeling the training data too closely, thus failing to generalize to new data. One way to combat overfitting is by **dropout**. In this technique, we temporarily remove units that we select at random during the learning phase. This way, we try to prevent over-reliance on any one unit in the network. Throughout training, the neural network will assume different forms, each time dropping some other units and then using them again:

![image-20221215092557013](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221215092557013.png)

### Computer Vision

Computer vision encompasses the different computational methods for analyzing and understanding digital images, and it is often achieved using neural networks.

Images consist of pixels, and pixels are represented by three values that range from 0 to 255, one for red, one for green and one for blue. These values are often referred to with the acronym RGB. We can use this to create a neural network where each color value in each pixel is an input, where we have some hidden layers, and the output is some number of units that tell us what it is that was shown in the image. 

However, there are a few drawbacks to this approach:

- First, by breaking down the image into pixels and the values of their colors, we can’t use the structure of the image as an aid. That is, as humans, if we see a part of a face we know to expect to see the rest of the face, and this quickens computation. We want to be able to use a similar advantage in our neural networks. 
- Second, the sheer number of inputs is very big, which means that we will have to calculate a lot of weights.

### Image Convolution

Image convolution is applying a filter that adds each pixel value of an image to its neighbors, weighted according to a kernel matrix. Doing so alters the image and can help the neural network process it.

Let’s consider the following example:

![image-20221215095353897](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221215095353897.png)

The kernel is the blue matrix, and the image is the big matrix on the left. The resulting filtered image is the small matrix on the bottom right.

Different kernels can achieve different tasks. For **edge detection**, the following kernel is often used:

![image-20221215095504940](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221215095504940.png)

The idea here is that when the pixel is similar to all its neighbors, they should cancel each other, giving a value of 0. Therefore, the more similar the pixels, the darker the part of the image, and the more different they are the lighter it is. Applying this kernel to an image (left) results in an image with pronounced edges (right):

![image-20221215095557669](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221215095557669.png)

Still, processing the image in a neural network is computationally expensive due to the number of pixels that serve as input to the neural network. Another way to go about this is **Pooling**, where the size of the input is reduced by sampling from regions in the input. Pixels that are next to each other belong to the same area in the image, which means that they are likely to be similar. Therefore, we can take one pixel to represent a whole area. One way of doing this is with **Max-Pooling**, where the selected pixel is the one with the highest value of all others in the same region. 

![image-20221215095717263](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221215095717263.png)

### Convolutional Neural Networks

![image-20221215101052236](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221215101052236.png)

A convolutional neural network is a neural network that uses convolution, usually for analyzing images. It starts by applying filters that can help distill some features of the image using different kernels. These filters can be improved in the same way as other weights in the neural network, by adjusting their kernels based on the error of the output. Then, the resulting images are pooled, after which the pixels are fed to a traditional neural network as inputs (a process called **flattening**).

![image-20221215101043627](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221215101043627.png)

The convolution and pooling steps can be repeated multiple times to extract additional features and reduce the size of the input to the neural network. One of the benefits of these processes is that, by convoluting and pooling, the neural network becomes less sensitive to variation. That is, if the same picture is taken from slightly different angles, the input for convolutional neural network will be similar, whereas, without convolution and pooling, the input from each image would be vastly different.

### Recurrent Neural Networks

Feed-Forward Neural Networks are the type of neural networks that we have discussed so far, where input data is provided to the network, which eventually produces some output. A diagram of how feed-forward neural networks work can be seen below.

![image-20221215101216920](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221215101216920.png)

As opposed to that, Recurrent Neural Networks consist of a non-linear structure, where the network uses its own output as input. For example, Microsoft’s captionbot is capable of describing the content of an image with words in a sentence. This is different from classification in that the output can be of varying length based on the properties of the image. While feed-forward neural networks are incapable of varying the number of outputs, **recurrent neural networks are capable to do that due to their structure**. In the captioning task, a network would process the input to produce an output, and then continue processing from that point on, producing another output, and repeating as much as necessary.

![image-20221215101330310](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221215101330310.png)

Recurrent neural networks are helpful in cases **where the network deals with sequences and not a single individual object**. Above, the neural network needed to produce a sequence of words. However, the same principle can be applied to analyzing video files, which consist of a sequence of images, or in translation tasks, where a sequence of inputs (words in the source language) is processed to produce a sequence of outputs (words in the target language).

## Language

**Natural Language Processing** spans all tasks where the AI gets human language as input. The following are a few examples of such tasks:

- automatic summarization, where the AI is given text as input and it produces a summary of the text as output.
- information extraction, where the AI is given a corpus of text and the AI extracts data as output.
- language identification, where the AI is given text and returns the language of the text as output.
- machine translation, where the AI is given a text in the origin language and it outputs the translation in the target language.
- named entity recognition, where the AI is given text and it extracts the names of the entities in the text (for example, names of companies).
- speech recognition, where the AI is given speech and it produces the same words in text.
- text classification, where the AI is given text and it needs to classify it as some type of text.
- word sense disambiguation, where the AI needs to choose the right meaning of a word that has multiple meanings (e.g. bank means both a financial institution and the ground on the sides of a river).

### Syntax and Semantics

**Syntax** is sentence structure.

**Semantics** is the meaning of words or sentences.

### Context-Free Grammar

![image-20221222104940244](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221222104940244.png)

- **Formal Grammar** is a system of rules for generating sentences in a language. 
- In **Context-Free Grammar**, the text is abstracted from its meaning to represent the structure of the sentence using formal grammar.



Let’s consider the following example sentence:

- She saw the city.

This is a simple grammatical sentence, and we would like to generate a syntax tree representing its structure. 

We start by assigning each word its part of speech. She and city are nouns, which we will mark as N. Saw is a verb, which we will mark as V. The is a determiner, marking the following noun as definite or indefinite, and we will mark it as D. Now, the above sentence can be rewritten as

- N V D N

So far, we have abstracted each word from its semantic meaning to its part of speech. However, words in a sentence are connected to each other, and to understand the sentence we must understand how they connect.

- A noun phrase (NP) is a group of words that connect to a noun. 
  - For example, the word *she* is a noun phrase in this sentence. In addition, the words *the city* also form a noun phrase, consisting of a determiner and a noun.
- A verb phrase (VP) is a group of words that connect to a verb. 
  - The word *saw* is a verb phrase in itself. However, the words *saw the city* also make a verb phrase. In this case, it is a verb phrase consisting of a verb and a noun phrase, which in turn consists of a determiner and a noun.
- Finally, the whole sentence (S) can be represented as follows:

![image-20221222105559848](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221222105559848.png)

### n-grams

An *n*-gram is a sequence of *n* items from a sample of text.

- In a **character *n*-gram**, the items are characters, and in a **word \*n\*-gram** the items are words.
- A *unigram*, *bigram*, and *trigram* are sequences of one, two, and three items. 

In the following sentence, the first three *n*-grams are “how often have,” “often have I,” and “have I said.”

“How often have I said to you that when you have eliminated the impossible whatever remains, however improbable, must be the truth?”

*n*-grams are useful for text processing. While the AI hasn’t necessarily seen the whole sentence before, it sure has seen parts of it, like “have I said.” Since some words occur together more often than others, it is possible to also predict the next word with some probability. For example, your smartphone suggests words to you based on a probability distribution derived from the last few words you typed. 

Thus, a helpful step in natural language processing is breaking the sentence into n-grams.

### Tokenization

Tokenization is the task of splitting a sequence of characters into pieces (tokens). Tokens can be words as well as sentences, in which case the task is called **word tokenization** or **sentence tokenization**. We need tokenization to be able to look at *n*-grams, since those rely on sequences of tokens.

We start by splitting the text into words based on the space character. While this is a good start, this method is imperfect because we end up with words with punctuation, such as “remains,”. So, for example, we can remove punctuation. However, then we face additional challenges, such as words with apostrophes (e.g. “o’clock”) and hyphens (e.g. “pearl-grey). Additionally, some punctuation is important for sentence structure, like periods. However, we need to be able to tell apart between a period at the end of the word “Mr.” and a period in the end of the sentence. Dealing with these questions is the process of tokenization. 

In the end, once we have our tokens, we can start looking at *n*-grams.

### Markov Models

Markov models consist of nodes, the value of each of which has a probability distribution based on a finite number of previous nodes. Markov models can be used to generate text. To do so, we train the model on a text, and then establish probabilities for every *n*-th token in an *n*-gram based on the *n* words preceding it. 

### Bag-of-Words Model

Bag-of-words is a model that represents text as an unordered collection of words. This model ignores syntax and considers only the meanings of the words in the sentence. This approach is helpful in some classification tasks, such as sentiment analysis (another classification task would be distinguishing regular email from spam email). Sentiment analysis can be used, for instance, in product reviews, categorizing reviews as positive or negative. 

Consider the following sentences:

1. “My grandson loved it! So much fun!”
2. “Product broke after a few days.”
3. “One of the best games I’ve played in a long time.”
4. “Kind of cheap and flimsy, not worth it.”

Based only on the words in each sentence and ignoring the grammar, we can see that sentences 1 and 3 are positive (“loved,” “fun,” “best”) and sentences 2 and 4 are negative (“broke,” “cheap,” “flimsy”).

### Naive Bayes

Naive Bayes is a technique that’s can be used in sentiment analysis with the bag-of-words model.

In sentiment analysis, we are asking “What is the probability that the sentence is positive/negative given the words in the sentence.” Answering this question requires computing conditional probability, and it is helpful to recall Bayes’ rule from lecture 2:

![image-20221222112412458](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221222112412458.png)

经过一定的化简：

![image-20221222130046424](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221222130046424.png)

One problem that we can run into is that some words may never appear in a certain type of sentence.

One way to go about this problem is with **Additive Smoothing**, where we add a value α to each value in our distribution to smooth the data. This way, even if a certain value is 0, by adding α to it we won’t be multiplying the whole probability for a positive or negative sentence by 0.

![image-20221222130300775](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221222130300775.png)

A specific type of additive smoothing, **Laplace Smoothing** adds 1 to each value in our distribution, pretending that all values have been observed at least once.

![image-20221222130308450](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221222130308450.png)

### Information Retrieval

Information retrieval is the task of finding relevant documents in response to a user query. To achieve this task, we use **topic modeling** to discover the topics for a set of documents. How can the AI go about extracting the topics of documents? One way to do so is by looking at **term frequency**, which is simply counting how many times a term appears in a document. The idea behind this is that key terms and important ideas are likely to repeat. To get term frequencies, we will work with the tf-idf library.

#### tf-idf

We can use the tf-idf library for information retrieval tasks. In lecture, we hoped to use term frequency to establish what the topics of each Sherlock Holmes story are in the corpus we had. However, when we ran the counting algorithm naively, the top-5 most common words were **function words**, words that are used for syntactic purposes in the sentence and not as independent units of meaning, such as “the,” “by,” “and,” “which,” “yet,” etc. By simply counting all the words by frequency of appearance we didn’t get the unique words that repeat in the corpus and define its topics, but the words that are the most common in the English language in general. The words that we are after are **content words**, words that carry meaning independently, such as “crime,” “brothers,” “demons,” “gentle,” “meek,” etc.

We can run the algorithm again, excluding words that we define as function words in the English language. Now the output becomes more indicative of the content of each document. However, in the case of Sherlock Holmes, the most common word in each document is, unsurprisingly, Holmes. Since we are searching the corpus of Sherlock Holmes story, having Holmes as one of the key words tells us nothing new about each story. This brings us to the idea of **Inverse Document Frequency**, which is **a measure of how common or rare a word is across documents in a corpus**. It is usually computed by the following equation:

![image-20221222152216793](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221222152216793.png)

Note that when the word appears in all documents, the value inside the logarithm is 1, and log(1) = 0. This is where the name of the library comes from: **tf-idf stand for Term Frequency — Inverse Document Frequency**. What this library is able to do is to multiply the term frequency of each word by the inverse document frequency, thus getting a value for each word. The more common the word is in one document and the fewer documents it appears in, the higher its value will be. Alternatively, the less common the word is in a document and the more common it is across documents, the lower its value. This lets us get as output a list of words per document that are likely to span the main topics that define the document.

### Information Extraction

Information Extraction is the task of extracting knowledge from documents. So far, treating text with the bag-of-words approach was helpful when we wanted the AI to perform simple tasks, such as recognizing sentiment in a sentence as positive or negative, or retrieving the key words in a document. However, for a task like information extraction, where we need the AI to understand the connections between different words, the bag-of-words approach won’t get us very far.

- A possible task of information extraction can take the form of giving a document to the AI as input and getting a list of companies and the years when they were founded as output. One way we can go about this is providing the AI with a template, such as “When {company} was founded in {year}.” This will not get us perfect results, because not all information about companies and their years of foundation are written in precisely this format. Still, if the dataset is large enough, we will definitely come across sentences of precisely this form, which will allow the AI to extract this knowledge.
- A more advanced approach would be to give the AI an abstracted example like “Face-book, 2004,” and let it develop its own model to extract the data. By going through enough data, the AI will be able to infer possible templates for extracting information similar to the example.

Using templates, even if self-generated by the AI, is helpful in tasks like Information Extraction. However, if we want the AI to be able to produce text like a human, the AI needs to be able to understand not just templates, but how all words in the language relate to each other in their meanings.

### Word Representation

We want to represent word meanings in our AI. As we’ve seen before, it is convenient to provide input to the AI in the form of numbers. One way to go about this is by using **One-Hot Representation**, where each word is represented with a vector that consists of as many values as we have words. Except for a single value in the vector that is equal to 1, all other values are equal to 0. How we can differentiate words is by which of the values is 1, ending up with a unique vector per word. For example, the sentence “He wrote a book” can be represented as four vectors:

- [1, 0, 0, 0] (he)
- [0, 1, 0, 0] (wrote)
- [0, 0, 1, 0] (a)
- [0, 0, 0, 1] (book)

However, while this representation works in a world with four words, if we want to represent words from a dictionary, when we can have 50,000 words, we will end up with 50,000 vectors of length 50,000. This is incredibly inefficient. Another problem in this kind of representation is that we are unable to represent similarity between words like “wrote” and “authored.” Instead, we turn to the idea of **Distributed Representation**, where meaning is distributed across multiple values in a vector. With distributed representation, each vector has a limited number of values (much less than 50,000), taking the following form:

- [-0.34, -0.08, 0.02, -0.18, …] (he)
- [-0.27, 0.40, 0.00, -0.65, …] (wrote)
- [-0.12, -0.25, 0.29, -0.09, …] (a)
- [-0.23, -0.16, -0.05, -0.57, …] (book)

This allows us to generate unique values for each word while using smaller vectors. Additionally, now we are able to represent similarity between words by how different the values in their vectors are.

### Word2vec

**word2vec is an algorithm for generating distributed representations of words.** It does so by **Skip-Gram Architecture**, which is a neural network architecture for predicting context given a target word. In this architecture, the neural network has an input unit for every target word. A smaller, single hidden layer (e.g. 50 or 100 units, though this number is flexible) will generate values that represent the distributed representations of words. Every unit in this hidden layer is connected to every unit in the input layer. The output layer will generate words that are likely to appear in a similar context as the target words. Similar to what we saw in last lecture, this network needs to be trained with a training dataset using the backpropagation algorithm.

![image-20221222155515023](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20221222155515023.png)

This neural network turns out to be quite powerful. In the end, of the process, every word ends up being just a vector, or a sequence of numbers.

By themselves, these numbers don’t mean much. But by finding which other words in the corpus have the most similar vectors, we can run a function that will generate the words that are the most similar to the word *book*. In the case of this network it will be: book, books, essay, memoir, essays, novella, anthology, blurb, autobiography, audiobook. This is not bad for a computer! Through a bunch of numbers that don’t carry any specific meaning themselves, the AI is able to generate words that really are very similar to *book* not in letters or sounds, but in meaning! We can also compute the difference between words based on how different their vectors are. For example, the difference between *king* and *man* is similar to the difference between *queen* and *woman*. That is, if we add the difference between *king* and *man* to the vector for *woman*, the closest word to the resulting vector is *queen*! Similarly, if we add the difference between *ramen* and *japan* to *america*, we get *burritos*. By using neural networks and distributed representations for words, we get our AI to understand semantic similarities between words in the language, bringing us one step closer to AIs that can understand and produce human language.
