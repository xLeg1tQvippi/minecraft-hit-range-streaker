import math
from pynput import mouse
import minescript

class CombatStreaker:
    def __init__(self):
        self.max_hit_length = 3.32

        try:
            self.main()

        except Exception as error:
            minescript.echo(error)        

    def get_target_player_data(self):
        return minescript.player_get_targeted_entity()
    
    def get_player_position(self) -> list[float, float, float]:
        return [round(pos, 1) for pos in minescript.player_position()]
    
    def get_target_player_position(self) -> list[float, float, float]:
        return [round(pos, 1) for pos in minescript.player_get_targeted_entity().position]
    
    def calculate_distance(self, own_pos: list[float], target_pos: list[float]) -> float:
        try:
            x1, y1, z1 = own_pos
            
            x2, y2, z2 = target_pos
        
            x = x1 - x2,
            y = y1 - y2
            z = z1 - z2
        
        except Exception as error:
            print(error)
        
        else:
            return [x, y, z]
    
    def get_distance_between_players(self, current_player_pos: list[float, float, float], target_player_pos: list[float, float, float]) -> float:
        try:
            # pos_differnce = self.calculate_distance(current_player_pos, target_player_pos)
            return math.dist(current_player_pos, target_player_pos)
            # return np.array(target_player_pos) - np.array(current_player_pos)
        except Exception as error:
            minescript.echo(error)
    
    def output_hit_marker(self, distance_difference: float):
        try:
            if distance_difference <= self.max_hit_length:                
                if distance_difference < 1.5:
                    minescript.echo('§f[hit] §8Bad!')
                if distance_difference >= 1.5 and distance_difference <= 2:
                    minescript.echo('§f[hit] §2Not bad!')
                elif distance_difference > 2 and distance_difference < 2.50:
                    minescript.echo("§f[hit] §aCool!")
                elif distance_difference > 2.50 and distance_difference < 2.85:
                    minescript.echo("§f[hit] §сNice!")
                elif distance_difference > 2.85 < distance_difference < 3.20:
                    minescript.echo("§f[hit] §e~Perfect~")
                elif distance_difference >= 3.20 and distance_difference <= self.max_hit_length:
                    minescript.echo("§f[hit] §5§k1§5§lChaotic hit!§k1")
                
        
        except Exception as error:
            pass
    
    def on_hit(self, x, y, button, pressed):
        try:
            if pressed:
                if button == mouse.Button.left:
                    target_data = self.get_target_player_data()
                        
                    if target_data != None and target_data.type == 'entity.minecraft.player':
                        current_player_pos = self.get_player_position()
                        target_player_pos = self.get_target_player_position()
                        # print("your coords:", *current_player_pos)
                        # print("target pos:", *target_player_pos)
                        self.get_target_player_data()
                        distance_difference = self.get_distance_between_players(current_player_pos, target_player_pos)
                        # minescript.echo('hit!')
                        self.output_hit_marker(distance_difference=distance_difference)
                    else:
                        minescript.echo('§7miss!')
                        
        except Exception: pass
        
    
    def main(self):
        try:
            with mouse.Listener(on_click=self.on_hit) as listener:
                listener.join()
        
        except Exception as error:
            print(error)

if __name__ == '__main__':
    try:
        print("Weclome to CombatStriker ^^")
        CombatStriker()
    except Exception as error:
        print(error)


