# import packages
import os
from cmdstanpy import cmdstan_path, CmdStanModel

# specify Stan program file
bernoulli_stan = os.path.join(cmdstan_path(), 'examples', 'bernoulli', 'bernoulli.stan')

# instantiate the model; compiles the Stan program as needed.
bernoulli_model = CmdStanModel(stan_file=bernoulli_stan)

# inspect model object
print(bernoulli_model)

# specify data file
bernoulli_data = os.path.join(cmdstan_path(), 'examples', 'bernoulli', 'bernoulli.data.json')

# fit the model
bern_fit = bernoulli_model.sample(data=bernoulli_data, output_dir='.')

# printing the object reports sampler commands, output files
print(bern_fit)

bern_fit.draws().shape
bern_fit.draws(concat_chains=True).shape

bern_fit.summary()


