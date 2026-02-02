import arcade 

window = arcade.Window( width= 1080, height= 1080, title= "Arcade")
arcade.start_render()
arcade.draw_circle_filled(center_x= 540, center_y= 540, radius= 200, color=arcade.color.YELLOW)
arcade.draw_ellipse_filled(center_x= 540, center_y= 400, width= 75,height= 65, color=arcade.color.DARK_CANDY_APPLE_RED)
arcade.draw_ellipse_filled(center_x= 540, center_y= 400, width= 70,height= 60, color=arcade.color.RED)
arcade.draw_line(start_x=540-35, start_y= 400, end_x= 605-30, end_y=400,color= arcade.color.DARK_CANDY_APPLE_RED, line_width= 4)
arcade.draw_circle_filled(center_x= 480, center_y= 580, radius= 40, color=arcade.color.WHITE)
arcade.draw_circle_filled(center_x= 600, center_y= 580, radius= 40, color=arcade.color.WHITE)
arcade.draw_circle_filled(center_x= 480, center_y= 580, radius= 15, color=arcade.color.BLACK)
arcade.draw_circle_filled(center_x= 600, center_y= 580, radius= 15, color=arcade.color.BLACK)
arcade.draw_line(start_x=540, start_y= 540, end_x= 520, end_y=500,color= arcade.color.DARK_CANDY_APPLE_RED, line_width= 4)
arcade.draw_line(start_x=540, start_y= 540, end_x= 520, end_y=500,color= arcade.color.DARK_CANDY_APPLE_RED, line_width= 4)

arcade.finish_render()
arcade.run()

print("hello world")