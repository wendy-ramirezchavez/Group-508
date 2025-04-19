def upgrade(player_level,completed_tasks, daily_tasks, max_level=10):
    need_tasks = daily_tasks.get(player_level,[])

    for task in need_tasks:
        if task not in completed_tasks:
            return player_level, [], {"finish all the task to level up"}
    
    player_level +=1
    tasks_unlock = daily_tasks.get(player_level,[])
    
    rewards = {}
    if 1<= player_level <= 4:
        rewards["starter_kit"] = True
    elif 5 <= player_level <= 9:
        rewards["upgrade_crops"] = True
    else: 
        rewards["premium_market"] = True
        
    return player_level, tasks_unlock, rewards
        
        # Some daily tasks for each level
daily_task = {
    1: ["watering", "fertilizing"],
    2: ["protecting", "harvesting"],
    3: ["watering", "harvesting", "fertilizing"]
}

if __name__ == "__main__":
    player_level = 1
    completed_tasks = ["watering", "fertilizing"]
    new_level, tasks_unlock, rewards = upgrade(player_level,completed_tasks, daily_task)
    
    print("New Level:", new_level)
    print("Unlock Tasks:", tasks_unlock)
    print("Rewards:", rewards)