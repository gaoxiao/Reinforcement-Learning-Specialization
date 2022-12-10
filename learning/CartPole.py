import gym
env = gym.make("CartPole-v1", render_mode="human", new_step_api=True)
env.action_space.seed(42)

observation = env.reset(seed=42)

for _ in range(300):
    observation, reward, terminated, truncated, info = env.step(env.action_space.sample())

    if terminated or truncated:
        print(f'reset')
        observation = env.reset()

env.close()
