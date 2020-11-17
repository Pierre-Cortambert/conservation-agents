import gym
import gym_fishing
from stable_baselines3 import PPO
from stable_baselines3.common.evaluation import evaluate_policy
from leaderboard import leaderboard, hash_url
import os
url = hash_url(os.path.basename(__file__)) # get hash URL at start of execution

ENV = "fishing-v1" # can do cts or discrete
env = gym.make(ENV)
model = PPO('MlpPolicy', env, verbose=0, tensorboard_log="/var/log/tensorboard/vec", device = "cpu")
model.learn(total_timesteps=300000)

## simulate and plot results
df = env.simulate(model, reps=10)
env.plot(df, "results/ppo.png")


base = gym.make(ENV, r = 0.1)
df = base.simulate(model, reps=10)
base.plot(df, "results/ppo-transfer.png")

## retrain on new env
model.learn(total_timesteps=300000, eval_env = env2)
df = base.simulate(model, reps=10)
env2.plot(df, "results/ppo-relearn.png")



## Evaluate model
# mean_reward, std_reward = evaluate_policy(model, env, n_eval_episodes=50)
# leaderboard("PPO", ENV, mean_reward, std_reward, url)


# model.save("models/ppo")
# print("mean reward:", mean_reward, "std:", std_reward)
