import argparse

import gym
import gym_conservation
from stable_baselines3.common.env_util import make_vec_env

import sys
sys.path.append("tuning")
from parse_hyperparameters import ppo_best, a2c_best, td3_best, sac_best, ddpg_best



def main():  # noqa: C901
    parser = argparse.ArgumentParser()
    parser.add_argument("--env", help="environment ID", type=str, default="CartPole-v1")
    parser.add_argument("-f", "--folder", help="Log folder", type=str, default="logs")
    parser.add_argument("--algo", help="RL Algorithm", default="ppo", type=str, required=False)
    parser.add_argument("-n", "--n-timesteps", help="number of timesteps", default=100000, type=int)
    parser.add_argument("--n-envs", help="number of environments", default=4, type=int)
    parser.add_argument("--verbose", help="Verbose mode (0: no output, 1: INFO)", default=1, type=int)
    parser.add_argument("--seed", help="Random generator seed", type=int, default=0)
    parser.add_argument("-tb", "--tensorboard-log", help="Tensorboard log dir", default="", type=str)

    args = parser.parse_args()


    env = gym.make(args.env)
    if args.algo in ["ppo", "a2c"]:
      env = make_vec_env(args.env, n_envs=args.n_envs, seed=args.seed)
    tune_best(args.algo, env, log_dir = args.f, tensorboard_log = args.tensorboard_log, seed = args.seed, verbose = args.verbose)

