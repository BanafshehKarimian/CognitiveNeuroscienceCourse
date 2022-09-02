# CognitiveNeuroscienceCourse
In this repository the projects that I have done for the cognitive neuroscience course are presented.
### Project1
In this project, I designed a test in order to investigate spatial heterogeneity in face perception and analyze whether the location of the stimuli has influence on detecting the gender using Psychophysics Toolbox. In the second phase, I first cleaned the data and added required columns and then exploed data through plotting multiple bar charts. After that, we used multivariable linear regression to predict behavioural characteristics. We plotted psychometric function per subject next, and calculated PSE (point of subjective equivalende) per visual field, per location and per ecc (eccentricity). We observed that: 1) the response time is smaller for the first visual field. One example of psychometric function is as follows:
The following figure demonstrates that for some locations subjects detected the stimuli as female more than others. They are more biased to female when PSE is closer to 1.
### Project2
In this project we implemented morris lecar, Hodgkin Huxley, LIF and WilsonCowan models that describe the initiation and propagation of action potentials in neurons.
For murris lecar the following plot shows V w.r.t n for I before and after action potential. For I = Ith only one action potential is initiated and for I > Ith more are initiated.
For LIF the amplitude of subthreshold oscillations of the membrane w.r.t. the input frequency and V w.r.t n for I before and after action potential are shown in the following plots. We can say that as the frequency increases, the amplitude of subthreshold oscillations of the membrane decreases.
For WilsonCowan activity of exitatory and inhibitory populations are ploted as follows. We can observe that they start from the same point but end with different values through different trajectories. 
For Hodgkin Huxley the changes of n (related to probability of K channels being open), m and h (related to probability of Na channels being open) w.r.t time and compare the V to capacity and see that with the increase of capacitor the action potential voltage threshol is reduced.
### Project3
In this peoject the paper "Najar A, Bonnet E, Bahrami B, Palminteri S. The actions of others act as a pseudo-reward to drive imitation in the context of social reinforcement learning. PLoS Biol. 2020 Dec 8;18(12):e3001028. doi: 10.1371/journal.pbio.3001028. PMID: 33290387; PMCID: PMC7723279." is implemented. 
The paper presents four models that people might use while learning socially: Decision Biasing, Model Based, value shaping and meta value shaping. VBA Toolbox is used to plot some of the plots. The result of my implementation compared to the paper's is as follows:
