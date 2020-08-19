import minerl
import gym
env = gym.make('MineRLNavigateDense-v0')

#reset the env to fisrt position
obs  = env.reset()

#Set done flag to false to initilize
done = False

#Intilaize the reward to 0
net_reward = 0

# loop until not done
while not done:

    #Dummy action that does nothing
    action = env.action_space.noop()

    #set the POV to compass angle
    action['camera'] = [0, 0.03*obs["compassAngle"]]
    
    # Go forward jump and attark
    action['back'] = 0
    action['forward'] = 1
    action['jump'] = 1
    action['attack'] = 1

    #update the observation based on the action, get the reward, 	
    obs, reward, done, info = env.step(
        action)
    
    #Accumilate and Print the Reward
    net_reward += reward
    print("Total reward: ", net_reward)



