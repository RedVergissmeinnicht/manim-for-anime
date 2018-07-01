from big_ol_pile_of_manim_imports import *
from once_useful_constructs.light import *

def plane_wave_homotopy(x, y, z, t):
    norm = np.linalg.norm([x, y])
    tau = interpolate(5, -5, t) + norm/FRAME_X_RADIUS
    alpha = sigmoid(tau)
    return [x, y + 0.5*np.sin(2*np.pi*alpha)-t*SMALL_BUFF/2, z]

dir_to_ind = {"u":0, "r":1, "d":2, "l":3}
dir_to_con = {"u":"d", "r":"l", "d":"u", "l":"r"}
dir_to_hat = {"u":UP, "r":RIGHT, "d":DOWN, "l":LEFT}
q_to_col = {"1":GREEN_E, "0.9":GREEN_D, "0.81":GREEN_C, "0.729":GREEN_B, "0.6561":GREEN_A, "0.59049":WHITE,
            "-1":RED_E, "-0.9":RED_D, "-0.81":RED_C, "-0.729":RED_B, "-0.6561":RED_A, "-0.59049":WHITE}

pq_map = [1, 0.9, 0.81, 0.729, 0.6561, 0.59049, 0.531441]
nq_map = [-1, -0.9, -0.81, -0.729, -0.6561, -0.59049, -0.531441]
nq_map.reverse()
q_map = pq_map + nq_map

SHIFT_CONSTANT = 0.45
hat_to_pos = {"u":SHIFT_CONSTANT*RIGHT, "r":SHIFT_CONSTANT*UP, "d":SHIFT_CONSTANT*LEFT, "l":SHIFT_CONSTANT*DOWN}

arrows = VMobject(Vector([0, 1]).set_color(WHITE), 
                          Vector([1, 0]).set_color(WHITE),
                          Vector([0, -1]).set_color(WHITE), 
                          Vector([-1, 0]).set_color(WHITE)
                          )
arrows.scale(0.7)
def ar(direction, x, y, q = None):
    imaging_pi = Randolph().scale_to_fit_height(1)
    imaging_pi.shift(1*LEFT+1*DOWN)
    imaging_pi.shift(2*x*RIGHT+2*y*UP)
    arrow = arrows[dir_to_ind[direction]].copy().next_to(imaging_pi, dir_to_hat[direction])
    if q == None:
        pass
    else:
        lable = TexMobject(str(q)).set_color(q_to_col[str(q)]).move_to(arrow)
        arrow.add(lable)
    return arrow

def twar(direction, x, y, q):
    imaging_pi = Randolph().scale_to_fit_height(1)
    imaging_pi.shift(1*LEFT+1*DOWN)
    imaging_pi.shift(2*x*RIGHT+2*y*UP)
    arrow1 = arrows[dir_to_ind[direction]].copy().next_to(imaging_pi, dir_to_hat[direction]
                ).shift(hat_to_pos[direction])
    arrow2 = arrows[dir_to_ind[dir_to_con[direction]]].copy().next_to(imaging_pi, dir_to_hat[direction]
                ).shift(hat_to_pos[dir_to_con[direction]])
    lable1 = TexMobject(str(q)).set_color(q_to_col[str(q)]).move_to(arrow1)
    lable2 = TexMobject(str(q_map[q_map.index(q) + 1])).set_color(q_to_col[str(q_map[q_map.index(q) + 1])]
                ).move_to(arrow2)    
    for stuff in [arrow2, lable1, lable2]:
        arrow1.add(stuff)
    return arrow1

RUSH_RUNTIME = 0.3
SUPER_RUSH_RUNTIME = 0.1

D1 = VGroup(*map(TextMobject, [
            "Disclaimer: Unfortunately, 3b1b does not",
            "seem to be happy about sharing his lovely pi creature.",
            "All pi creature expressions were banned",
            "except for this boring, dull plain expression,",
            "which results in this dummy-like pi creature agent.",
            "\#PiCreatureHasFeeling",
        ]))
D1.arrange_submobjects(DOWN, aligned_edge = LEFT).scale_to_fit_width(8).set_color(YELLOW).to_corner(UP+LEFT)
D2 = VGroup(*map(TextMobject, [
            "Disclaimer: The 3 minutes rule seems somewhat",
            "discourages videos that \"dive too deep into a topic,\"",
            "of which often requires a longer video length",
            "and occasionally slower the pace for more thought-provoking sections.",
            "I inevitably had to cut out or speed up some of my clips,",
            "and abandon more adorable pi creatures",
            "including more contents like Deep Q-learning and Markov Decision process.",
            "I will consider doing a full-length video if there are lots of demands."
        ]))
D2.arrange_submobjects(DOWN, aligned_edge = LEFT).scale_to_fit_width(8).set_color(YELLOW).to_corner(UP+LEFT)
D3 = VGroup(*map(TextMobject, [
            "Disclaimer: Actually, due to the complexity",
            "of go game(which is a result of the curse of dimensionality),",
            "pre-train the agent with all possible states and actions is impractical.",
            "AlphaGo not only used Reinforcement Learning",
            "but also combined the Supervise Learning",
            "(which can mimic human chess gameplay)",
            "and Monte Carlo Tree Search",
            "(which is effective for looking ahead several moves)",
        ]))
D3.arrange_submobjects(DOWN, aligned_edge = LEFT).scale_to_fit_width(8).set_color(YELLOW).to_corner(UP+LEFT)

D4 = TextMobject("ps:This map is incomplte").scale_to_fit_width(3).set_color(YELLOW).to_corner(UP+LEFT)

##############

# mousy.shift(2*LEFT)
# self.wait()
# self.play(Blink(mousy))
            
class Laboratory(LinearTransformationScene):
# generate maze and explaining agent
    CONFIG = {
        "include_background_plane" : False,
        "show_basis_vectors" : False,
    }
       
    def construct(self): # one block to construct them all!
        print("This will be the most terrible code you have ever seen:")
        self.setup()
        self.plane.prepare_for_nonlinear_transform()
        self.play(ShowCreation(
                               self.plane, 
                               submobject_mode = "one_at_a_time",
                               run_time = 0.5
                              )
                  )   
        mousy = Randolph().scale_to_fit_height(1)

        agent_lable = TexMobject("agent").shift(3*DOWN).scale(4).set_color(GRAY)

        pop = SVGMobject(file_name = "lollipop").rotate(90)
        pop.scale_to_fit_height(1)
        pop.set_fill(GREEN_C)        

        fire = SVGMobject(file_name = "fire")
        fire.scale_to_fit_height(1)
        fire.set_fill(RED)
        fire_2 = fire.deepcopy()

        rb_1 = SVGMobject(file_name = "roadblock").rotate(135.08) # This is stupid
        rb_1.scale_to_fit_height(1)
        rb_1.set_fill(DARK_GRAY)
#        rb_1_outline = rb_1.copy()
#        rb_1_outline.set_fill(opacity = 0)
#        rb_1_outline.set_stroke(BLACK, 3)
        rb_2 = rb_1.deepcopy()
        rb_3 = rb_1.deepcopy()
        
        pop.shift(4.9*RIGHT+UP)
        fire.shift(5*RIGHT+3*DOWN)  
        fire_2.shift(5*LEFT+1*UP)
        rb_1.shift(1*RIGHT+1*DOWN)         
        rb_2.shift(1*LEFT+3*UP)           
        rb_3.shift(3*LEFT+3*DOWN)           
        mousy.shift(3*LEFT+1*DOWN)
        
        for stuff in [pop, fire, fire_2, rb_1, rb_2, rb_3]:
            self.play(
                      DrawBorderThenFill(stuff),
                      run_time = 0.2
                     )                 
                                                       # Nice try ;(
        """
        p_lable = TexMobject("R\s =\s +1").scale_to_fit_height(0.4)
        n_lable = TexMobject("R\s =\s -1").scale_to_fit_height(0.4)
        p_lable[0].set_color(ORANGE)
        p_lable[2:3].set_color(GREEN)
        n_lable[0].set_color(ORANGE)
        n_lable[2:3].set_color(RED)        
                
        r_1 = None
        r_2 = None
        r_3 = None        
        for r_lable in [r_1, r_2, r_3]:
            for stuff in [pop, fire, fire_2]:                                      
                if stuff == pop:
                    r_lable = p_lable.next_to(stuff, 0.5*DOWN)
                    self.play(
                              Write(r_lable)                   
                             )
                    break
                else:
                    r_lable = n_lable.next_to(stuff, 0.5*DOWN)
                    self.play(
                              Write(r_lable)
                             )
                    break
         """       
        r_1 = TexMobject("R=+1").scale_to_fit_height(0.4).next_to(pop, 0.1*DOWN)
        r_2 = TexMobject("R=-1").scale_to_fit_height(0.4).next_to(fire, 0.2*DOWN)
        r_3 = TexMobject("R=-1").scale_to_fit_height(0.4).next_to(fire_2, 0.2*DOWN)
        for stuff in [r_1,r_2, r_3]:                   
            stuff[0].set_color(ORANGE)                  #This is inefficient and inelegant. Nevertheless, it works                       
        r_1[2:4].set_color(GREEN)
        r_1[-1].set_color(GREEN)
        r_2[2:4].set_color(RED)
        r_2[-1].set_color(RED)
        r_3[2:4].set_color(RED)
        r_3[-1].set_color(RED)
        
        self.play(
                  Write(r_1),
                  Write(r_2),
                  Write(r_3),
                  FadeIn(mousy),
                  Blink(mousy),
                  run_time = RUSH_RUNTIME
                 )
        
        for stuff in [mousy, pop, fire, fire_2, rb_1, rb_2, rb_3, r_1, r_2, r_3]:
            self.plane.add(stuff)

        self.play(Homotopy(plane_wave_homotopy, self.plane, run_time = 3)) 
 
        agent_arrow = Arrow(agent_lable.get_top(), mousy.get_bottom(), stroke_width = 1000)
        agent_arrow.set_color(GRAY)
        self.play(Blink(mousy))
        self.wait()
        
        self.play(Write(agent_lable),
                  GrowFromPoint(agent_arrow, agent_arrow.get_start())
                  )
        self.wait(2)
        self.remove(agent_lable)
        self.remove(agent_arrow)
        
# explaining states
        state_lable = TexMobject("state").shift(3*DOWN).scale(4).set_color(TEAL_E)
        self.play(Write(state_lable))
# fire  
        self.play(FadeOut(mousy), run_time = RUSH_RUNTIME)
        mousy.shift(8*RIGHT+2*DOWN)
        self.play(FadeIn(mousy), run_time = RUSH_RUNTIME)
        fr_1 = SVGMobject(file_name = "fire").set_fill(YELLOW).scale_to_fit_height(0.4)
        fr_2 = fr_1.deepcopy()
        fr_3 = fr_1.deepcopy()
        fr_1.next_to(mousy, UP).shift(0.3*LEFT+0.6*DOWN)
        fr_2.next_to(mousy, UP).shift(0.4*RIGHT+0.4*DOWN)
        fr_3.next_to(mousy, DOWN).shift(0.2*LEFT+0.7*UP)
        self.play(GrowFromPoint(fr_1, fr_1.get_bottom()),
                  GrowFromPoint(fr_2, fr_2.get_bottom()),
                  GrowFromPoint(fr_3, fr_3.get_bottom()),
                  )   
        self.add(D1)
        
        square = SurroundingRectangle(mousy, color = TEAL_E).scale_to_fit_height(self.plane.get_y_unit_size()*2)
        self.play(ShowCreation(square), run_time = RUSH_RUNTIME)
        self.play(FadeOut(square), run_time = RUSH_RUNTIME)
# pop        
        for stuff in [fr_1, fr_2, fr_3]:
            self.remove(stuff)
        self.play(FadeOut(mousy), run_time = RUSH_RUNTIME)
        mousy.shift(4*UP+2*LEFT)
        self.play(FadeIn(mousy), run_time = RUSH_RUNTIME)
        square = SurroundingRectangle(mousy, color = TEAL_E).scale_to_fit_height(self.plane.get_y_unit_size()*2)
        self.play(ShowCreation(square), run_time = RUSH_RUNTIME)
        self.play(FadeOut(square), run_time = RUSH_RUNTIME)
        self.remove(D1)
# middle of nowhere        
        self.play(FadeOut(mousy), run_time = RUSH_RUNTIME)
        mousy.shift(6*LEFT, 2*DOWN)
        self.play(FadeIn(mousy), run_time = RUSH_RUNTIME)
        square = SurroundingRectangle(mousy, color = TEAL_E).scale_to_fit_height(self.plane.get_y_unit_size()*2)
        self.play(ShowCreation(square), run_time = RUSH_RUNTIME)
        self.play(FadeOut(square), run_time = RUSH_RUNTIME)
        self.play(Blink(mousy))
        self.wait(3) #
# eat pop
        pop_for_pi = SVGMobject(file_name = "lollipop").set_fill(GREEN_B).rotate(90).scale_to_fit_height(0.4)
        self.play(FadeOut(mousy), run_time = RUSH_RUNTIME)
        mousy.shift(8*RIGHT+2*UP)
        self.play(FadeIn(mousy), run_time = RUSH_RUNTIME)
        pop_for_pi.next_to(mousy, UP).shift(0.6*RIGHT+0.4*DOWN)
        square = SurroundingRectangle(mousy, color = TEAL_E).scale_to_fit_height(self.plane.get_y_unit_size()*2)
        self.play(ShowCreation(square),
                  DrawBorderThenFill(pop_for_pi),
                  run_time = RUSH_RUNTIME)
        self.play(FadeOut(square), run_time = RUSH_RUNTIME)
        self.wait(2) #
        
        self.remove(pop_for_pi) 
        self.play(FadeOut(mousy), run_time = RUSH_RUNTIME)
        mousy.shift(8*LEFT+2*DOWN)
        self.play(FadeIn(mousy), run_time = RUSH_RUNTIME)       
        self.remove(state_lable)
# explaining actions
        action_lable = TexMobject("action").shift(3*DOWN).scale(4).set_color(YELLOW)
        self.play(Write(action_lable))
        self.wait(3) # 5 give real life examples
        
        
        arrows = VMobject(Vector([0, 1]).set_color(WHITE), 
                          Vector([1, 0]).set_color(WHITE),
                          Vector([0, -1]).set_color(WHITE), 
                          Vector([-1, 0]).set_color(WHITE)
                          )
        arrows.scale(0.75)
        arrows[0].next_to(mousy, UP)
        arrows[1].next_to(mousy, RIGHT)
        arrows[2].next_to(mousy, DOWN)
        arrows[3].next_to(mousy, LEFT)
        self.play(Blink(mousy))
        
        UP_lable = TexMobject("UP").next_to(arrows[0], UP)
        RIGHT_lable = TexMobject("RIGHT").next_to(arrows[1], RIGHT)
        DOWN_lable = TexMobject("DOWN").next_to(arrows[2], DOWN)
        LEFT_lable = TexMobject("LEFT").next_to(arrows[3], LEFT)

        self.play(Write(arrows), run_time = 0.5)
        
        for stuff in [UP_lable, RIGHT_lable, DOWN_lable, LEFT_lable]:
            self.play(FadeInFromDown(stuff), run_time = SUPER_RUSH_RUNTIME)
        for stuff in [UP_lable, RIGHT_lable, DOWN_lable, LEFT_lable]:
            self.play(FadeOut(stuff), run_time = RUSH_RUNTIME)
        
        
        arrows[1].set_color(YELLOW)
        for right in [2*RIGHT]:
            self.play(ApplyMethod(mousy.shift, right, run_time = 1))
        self.play(FadeOut(arrows), run_time = RUSH_RUNTIME)
        self.remove(arrows)
        arrows[1].set_color(WHITE)
        arrows[0].next_to(mousy, UP)
        arrows[1].next_to(mousy, RIGHT)
        arrows[2].next_to(mousy, DOWN)
        arrows[3].next_to(mousy, LEFT)
        self.play(Write(arrows), run_time = 0.5)
        
        arrows[0].set_color(YELLOW)
        for up in [2*UP]:
            self.play(ApplyMethod(mousy.shift, up, run_time = 1))
        self.play(FadeOut(arrows), run_time = RUSH_RUNTIME)
        self.remove(arrows)
        arrows[0].set_color(WHITE)
        arrows[0].next_to(mousy, UP)
        arrows[1].next_to(mousy, RIGHT)
        arrows[2].next_to(mousy, DOWN)
        arrows[3].next_to(mousy, LEFT)
        self.play(Write(arrows), run_time = 0.5)
        self.play(FadeOut(arrows), run_time = RUSH_RUNTIME)
        self.remove(arrows)
        
        self.remove(action_lable)
        self.wait()

# explaining good actions # and it was a silly idea
        """
        for lollipop in [2*UP, 6*RIGHT]:
            self.play(ApplyMethod(mousy.shift, lollipop, run_time = 0.2))
        arrows[1].next_to(mousy, RIGHT)
        self.play(Write(arrows[1]))
        self.wait() # 2
        self.play(FadeOut(arrows[1]))
        self.remove(arrows[1])
        for right in [2*RIGHT]:
            self.play(ApplyMethod(mousy.shift, right, run_time = 1))
        self.wait()
        self.play(mousy.change, "happy")
        self.wait() # 3
        for step in [8*LEFT, 2*DOWN]:
            self.play(ApplyMethod(mousy.shift, step, run_time = 0.2))
        for fire in [2*RIGHT, 2*DOWN, 4*RIGHT]:
            self.play(ApplyMethod(mousy.shift, fire, run_time = 0.2))
        arrows[1].next_to(mousy, RIGHT)
        self.play(Write(arrows[1])) 
        self.wait() # 3
        self.play(FadeOut(arrows[1]))
        self.remove(arrows[1])
        for right in [2*RIGHT]:
            self.play(ApplyMethod(mousy.shift, right, run_time = 1))
        self.wait()
        self.play(mousy.change, "angry")
        self.wait() # 3
        """
# explaining rewards
        reward_lable = TexMobject("reward").shift(3*DOWN).scale(4).set_color(ORANGE)
        self.play(FadeOut(mousy), run_time = RUSH_RUNTIME)
        mousy.shift(2*DOWN+6*RIGHT)
        self.play(FadeIn(mousy), run_time = RUSH_RUNTIME)
        self.play(Write(reward_lable),
                  Blink(mousy))
        
        arrows[0].next_to(mousy, UP)
        arrows[1].next_to(mousy, RIGHT)
        arrows[2].next_to(mousy, DOWN)
        arrows[3].next_to(mousy, LEFT)
        self.play(Write(arrows), run_time = SUPER_RUSH_RUNTIME)
        arrows[0].set_color(YELLOW)
        for up in [2*UP]:
            self.play(ApplyMethod(mousy.shift, up, run_time = SUPER_RUSH_RUNTIME))
        self.play(FadeOut(arrows), run_time = SUPER_RUSH_RUNTIME)        
        self.remove(arrows)        
        eat = TexMobject("Reward = +1").next_to(mousy, UP+12*LEFT).scale(2)
        eat[0: 6].set_color(ORANGE)
        eat[7: 9].set_color(GREEN)

        pop_for_pi = SVGMobject(file_name = "lollipop").set_fill(GREEN_B).rotate(90).scale_to_fit_height(0.4)
        pop_for_pi.next_to(mousy, UP).shift(0.6*RIGHT+0.4*DOWN)
                
        self.play(DrawBorderThenFill(pop_for_pi),
                  Write(eat),
                  mousy.change, "happy",
                  Blink(mousy),
                  run_time = 1
                  )
        self.wait()
        
        self.remove(eat)
        self.remove(pop_for_pi)

        arrows[0].set_color(WHITE)
        arrows[0].next_to(mousy, UP)
        arrows[1].next_to(mousy, RIGHT)
        arrows[2].next_to(mousy, DOWN)
        arrows[3].next_to(mousy, LEFT)
        self.play(Write(arrows), run_time = SUPER_RUSH_RUNTIME)
        arrows[2].set_color(YELLOW)        
        for down in [2*DOWN]:
            self.play(ApplyMethod(mousy.shift, down, run_time = SUPER_RUSH_RUNTIME))

        self.play(FadeOut(arrows), run_time = SUPER_RUSH_RUNTIME)        
        self.remove(arrows)            
        arrows[2].set_color(WHITE)
        arrows[0].next_to(mousy, UP)
        arrows[1].next_to(mousy, RIGHT)
        arrows[2].next_to(mousy, DOWN)
        arrows[3].next_to(mousy, LEFT)
        self.play(Write(arrows), run_time = SUPER_RUSH_RUNTIME)
        arrows[2].set_color(YELLOW)
        for down in [2*DOWN]:
            self.play(ApplyMethod(mousy.shift, down, run_time = SUPER_RUSH_RUNTIME))            

        arrows[2].set_color(WHITE)            
        self.play(FadeOut(arrows), run_time = SUPER_RUSH_RUNTIME)        
        self.remove(arrows)            
        burn = TexMobject("Reward = -1").next_to(mousy, 2*UP+12*LEFT).scale(2)
        burn[0: 6].set_color(ORANGE)
        burn[7: 9].set_color(RED)
        fr_1 = SVGMobject(file_name = "fire").set_fill(YELLOW).scale_to_fit_height(0.4)
        fr_2 = fr_1.deepcopy()
        fr_3 = fr_1.deepcopy()
        fr_1.next_to(mousy, UP).shift(0.3*LEFT+0.6*DOWN)
        fr_2.next_to(mousy, UP).shift(0.4*RIGHT+0.4*DOWN)
        fr_3.next_to(mousy, DOWN).shift(0.2*LEFT+0.7*UP)

        self.play(mousy.change, "angry")
        self.play(GrowFromPoint(fr_1, fr_1.get_bottom()),
                  GrowFromPoint(fr_2, fr_2.get_bottom()),
                  GrowFromPoint(fr_3, fr_3.get_bottom()),
                  Write(burn),
                  Blink(mousy),
                  run_time = 1,) 
        self.wait()
        
        for stuff in [fr_1, fr_2, fr_3, burn, arrows]:
            self.remove(stuff)
        arrows[2].set_color(WHITE)
        for up in [2*UP]:
            self.play(ApplyMethod(mousy.shift, up, run_time = SUPER_RUSH_RUNTIME))
        for left in [2*LEFT]:
            self.play(ApplyMethod(mousy.shift, left, run_time = SUPER_RUSH_RUNTIME))
        arrows[0].next_to(mousy, UP)
        arrows[1].next_to(mousy, RIGHT)
        arrows[2].next_to(mousy, DOWN)
        arrows[3].next_to(mousy, LEFT)
        self.play(Write(arrows), run_time = SUPER_RUSH_RUNTIME)
        arrows[3].set_color(YELLOW)
        for block in [1*LEFT, 1*RIGHT]:
            self.play(ApplyMethod(mousy.shift, block, run_time = 0.3))
        self.play(mousy.change, "confused")
        self.wait()
        self.remove(arrows)
        arrows[3].set_color(WHITE)
#        self.wait(3) #     
        
#        self.wait(3) #
        self.remove(reward_lable)

# explaining bellman equation
        for stuff in [fire, fire_2, rb_1, rb_2, rb_3, r_2, r_3]:
            self.remove(stuff)
        mousy.shift(2*UP)
        self.play(FadeIn(mousy), run_time = RUSH_RUNTIME)
        self.play(mousy.change, "plain", run_time = RUSH_RUNTIME)
        self.play(Blink(mousy))
        self.wait(4) #
        arrows[0].next_to(mousy, UP)
        arrows[1].next_to(mousy, RIGHT)
        arrows[2].next_to(mousy, DOWN)
        arrows[3].next_to(mousy, LEFT)
        self.play(Write(arrows), run_time = RUSH_RUNTIME)
        self.wait(2)
        
        confused = TextMobject(
            "Which ",
            "action ",
            "should ",
            "I ",
            "choose!?",
        )
        confused.set_color_by_tex_to_color_map({
                "action":YELLOW,
                "I":GRAY})
        self.play(PiCreatureSays(
                mousy, confused,    
                target_mode = "angry",
                play_time = 2
                ))
        self.wait()
        self.play(RemovePiCreatureBubble(mousy),
                  mousy.change, "pondering")
        
        needs_for_bellman = TextMobject(
                "In the current",
                "state,\\\ ",
                "the",
                "best",
                "action",
                "is to go right",
                alignment = ""
                ).scale(2).to_corner(DOWN)
        needs_for_bellman.set_color_by_tex_to_color_map({        # This method is so awful to use 
                "action":YELLOW,
                "state":TEAL_E,
                "best":MAROON
                })  
        rttttt = TextMobject(
                "I ",
                "should ",
                "go right",
                "!")
        rttttt[0].set_color(GRAY)
        rttttt[2].set_color(YELLOW)
               
        self.play(FadeOut(arrows), run_time = RUSH_RUNTIME)
        self.remove(arrows)
        arrows[1].set_color(YELLOW)
        self.play(PiCreatureSays(
                mousy, rttttt,    
                target_mode = "surprised",),
                Write(needs_for_bellman))
        self.play(GrowFromPoint(arrows[1], arrows[1].get_start()), run_time = RUSH_RUNTIME)
        for right in [2*RIGHT]:
            self.play(ApplyMethod(mousy.shift, right, run_time = 1))
        eat = TexMobject("Reward = +1").next_to(mousy, UP+12*LEFT).scale(2)
        eat[0: 6].set_color(ORANGE)
        eat[7: 9].set_color(GREEN)
        pop_for_pi = SVGMobject(file_name = "lollipop").set_fill(GREEN_B).rotate(90).scale_to_fit_height(0.4)
        pop_for_pi.next_to(mousy, UP).shift(0.6*RIGHT+0.4*DOWN)
         
        self.play(RemovePiCreatureBubble(mousy),
                  mousy.change, "happy",
                  run_time = RUSH_RUNTIME)
        self.play(DrawBorderThenFill(pop_for_pi),
                  Write(eat),
                  Blink(mousy), run_time = RUSH_RUNTIME)        
        self.wait() # 5
        self.remove(arrows[1])
        self.remove(eat)
        self.remove(needs_for_bellman)
        self.remove(pop_for_pi)
        
        for down in [2*LEFT+4*DOWN]:
            self.play(ApplyMethod(mousy.shift, down, run_time = 1))
        rttttt2 = TextMobject(
                "I ",
                "shouldn't ",
                "go right",
                "!")
        rttttt2[0].set_color(GRAY)
        rttttt2[2].set_color(YELLOW)
        r_2 = TexMobject("R=-1").scale_to_fit_height(0.4).next_to(fire, 0.2*DOWN)
        self.play(PiCreatureSays(
                mousy, rttttt2,    
                target_mode = "angry",),
        FadeIn(fire),
        FadeIn(r_2))
        self.wait()    

class WheresTheLearning(TeacherStudentsScene):
    def construct(self):
       self.wheres()
    def wheres(self):
        self.student_says(
                "Where's the learning!?",
                run_time = 1
                )
        self.change_student_modes(
                "angry",
                "angry",
                "angry"
                )        

# trying to write a more "readable" code
        
class Discussion(TeacherStudentsScene):
    def construct(self):
       self.raise_the_needs()

    def raise_the_needs(self):
        suggestion_1 = TextMobject(
            "We can define \\\\ a",
            "$function$ ",
            "that measure \\\\ the",
            "$quality$",
            "of an",
            "action \\\\ ",
            "in a certain",
            "state",  
        )
        suggestion_1.set_color_by_tex_to_color_map({        # This method is so awful to use 
                "function":MAROON,
                "quality":MAROON,
                "action":YELLOW,
                "state":TEAL_E
                })  

        suggestion_2 = TextMobject(
            "And name it ", "Q","(","s",",","a",")"
        )
        suggestion_2[1].set_color(MAROON)
        suggestion_2[3].set_color(TEAL_E)
        suggestion_2[5].set_color(YELLOW)
        
        suggestion_3 = TextMobject(
            "so that the higher the", "Q","(","s",",","a",")","of","an","action","is\\\\ ",
            "the better the ","action"
        )
        suggestion_3.set_color_by_tex_to_color_map({       
                    "action":YELLOW,
                    })
        suggestion_3[1].set_color(MAROON)
        suggestion_3[3].set_color(TEAL_E)
        suggestion_3[5].set_color(YELLOW)  
        
        tec = TextMobject(
            "Some","actions","are better than","others"   
        )
        tec.set_color_by_tex_to_color_map({       
                "action":YELLOW,
                "others":YELLOW
                })  
        tec2 = TextMobject(
            "And we are going to use that"   
        )

        self.teacher_says(
                tec,
                run_time = 3
                )    
        self.teacher_says(
                tec2,
                run_time = 3
                )    
        self.student_says(
                suggestion_1,
                run_time = 3
                )
        self.change_student_modes(
                "speaking",
                "raise_right_hand"
                )
        self.student_says(
                suggestion_2,
                run_time = 2
                )
        self.student_says(
                suggestion_3,
                run_time = 3
                )
        self.change_student_modes(
                "pondering"
                )
        self.wait()

QR_expr = TexMobject(
"Q","(","s",",","a",") = ","R",
                              alignment = '').scale_to_fit_width(8)
QR_expr.set_color_by_tex_to_color_map({       
                    "Q":MAROON,
                    "s":TEAL_E,
                    "a":YELLOW,                  
                    "R":ORANGE,
                    "pha":PURPLE_A,
                    "\gamma":PURPLE_D,
                    "max":MAROON,
                    })
Q, o, s, comma, a, pequals, R = QR_expr

class ManInBell1(LinearTransformationScene):
    CONFIG = {
        "include_background_plane" : False,
        "show_basis_vectors" : False,
        "include_foreground_plane": False
    }
       
    def construct(self):
        self.show_equation()
        self.put_into_play()

        
    def show_equation(self):      
        self.play(Write(QR_expr), play_time = 2)
        brace = Brace(R, UP, buff = SMALL_BUFF)
        text = brace.get_text(
            "Reward",
            buff = SMALL_BUFF
        ).set_color(ORANGE)
        self.play(GrowFromCenter(brace),
            Write(text, run_time = 2),
        )
        brace.add(text)                
        self.wait()
        self.remove(text)
        self.play(FadeOut(brace), run_time = SUPER_RUSH_RUNTIME)
        
    def put_into_play(self):        
        self.play(QR_expr.scale, 0.6,
                  QR_expr.to_corner, UP+LEFT,
            )
        self.add_plane()
        self.add(QR_expr)
# ctrl+c & ctrl+v zone start
        mousy = Randolph().scale_to_fit_height(1)

        pop = SVGMobject(file_name = "lollipop").rotate(90)
        pop.scale_to_fit_height(1)
        pop.set_fill(GREEN_C)        

        fire = SVGMobject(file_name = "fire")
        fire.scale_to_fit_height(1)
        fire.set_fill(RED)
        fire_2 = fire.deepcopy()

        rb_1 = SVGMobject(file_name = "roadblock").rotate(135.08) 
        rb_1.scale_to_fit_height(1)
        rb_1.set_fill(DARK_GRAY)
        rb_2 = rb_1.deepcopy()
        rb_3 = rb_1.deepcopy()
        
        pop.shift(4.9*RIGHT+UP)
        fire.shift(5*RIGHT+3*DOWN)  
        fire_2.shift(5*LEFT+1*UP)
        rb_1.shift(1*RIGHT+1*DOWN)         
        rb_2.shift(1*LEFT+3*UP)           
        rb_3.shift(3*LEFT+3*DOWN)           
        mousy.shift(3*RIGHT+1*UP)

        r_1 = TexMobject("R=+1").scale_to_fit_height(0.4).next_to(pop, 0.1*DOWN)
        r_2 = TexMobject("R=-1").scale_to_fit_height(0.4).next_to(fire, 0.2*DOWN)
        r_3 = TexMobject("R=-1").scale_to_fit_height(0.4).next_to(fire_2, 0.2*DOWN)
        for stuff in [r_1,r_2, r_3]:                   
            stuff[0].set_color(ORANGE)                                       
        r_1[2:4].set_color(GREEN)
        r_1[-1].set_color(GREEN)
        r_2[2:4].set_color(RED)
        r_2[-1].set_color(RED)
        r_3[2:4].set_color(RED)
        r_3[-1].set_color(RED)        
# ctrl+c & ctrl+v zone end   
        self.play(
                  FadeInFromDown(pop),
                  FadeInFromDown(fire),
                  FadeInFromDown(rb_1),
                  FadeInFromDown(rb_2),
                  FadeInFromDown(rb_3),
                  FadeInFromDown(fire_2),
                  FadeInFromDown(r_1),
                  FadeInFromDown(r_2),
                  FadeInFromDown(r_3),
                  FadeInFromDown(mousy)
                  )  
        self.add(QR_expr)
        rect = SurroundingRectangle(QR_expr)
        rect.set_color_by_gradient(RED, YELLOW)
        self.play(ShowCreation(rect))

# find path
        reward_answer = TexMobject("randomly\, decided\, to\, go\, right").shift(2*DOWN).scale(1.5)
        reward_answer[-7:-1].set_color(YELLOW)
        reward_answer[-1].set_color(YELLOW)
        self.play(Write(reward_answer))
        
        arrows = VMobject(Vector([0, 1]).set_color(WHITE), 
                          Vector([1, 0]).set_color(WHITE),
                          Vector([0, -1]).set_color(WHITE), 
                          Vector([-1, 0]).set_color(WHITE)
                          )
        arrows.scale(0.75)
        arrows[0].next_to(mousy, UP)
        arrows[1].next_to(mousy, RIGHT)
        arrows[2].next_to(mousy, DOWN)
        arrows[3].next_to(mousy, LEFT)
        self.play(Write(arrows))
        
        arrows[1].set_color(YELLOW)
        self.play(DrawBorderThenFill(arrows[1]), run_time = RUSH_RUNTIME)
        
        for right in [2*RIGHT]:
            self.play(ApplyMethod(mousy.shift, right, run_time = 1))
        eat = TexMobject("Reward = +1").next_to(mousy, UP+12*LEFT).scale(2)
        eat[0: 6].set_color(ORANGE)
        eat[7: 9].set_color(GREEN)
        pop_for_pi = SVGMobject(file_name = "lollipop").set_fill(GREEN_B).rotate(90).scale_to_fit_height(0.4)
        pop_for_pi.next_to(mousy, UP).shift(0.6*RIGHT+0.4*DOWN)
         
        self.play(mousy.change, "happy", run_time = RUSH_RUNTIME)
        self.play(DrawBorderThenFill(pop_for_pi),
                  Write(eat),
                  Blink(mousy))

        arrows[1].set_color(WHITE)        
        self.play(FadeOut(mousy),
                  FadeOut(pop_for_pi),
                  FadeOut(reward_answer),
                ReplacementTransform(
                VGroup(eat),
                VGroup(VGroup(R))))
        Q1 = TexMobject("Q","(","s",",","a",")=","1").next_to(arrows[1])
        Q1.set_color_by_tex_to_color_map({       
                    "Q":MAROON,
                    "s":TEAL_E,
                    "a":YELLOW,                  
                    "R":ORANGE,
                    "pha":PURPLE_A,
                    "\gamma":PURPLE_D,
                    "max":MAROON,
                    "1":GREEN,
                    "-":RED,
                    "0":DARK_GRAY
                    })
        self.play(
                ReplacementTransform(
                VGroup(QR_expr).copy(),
                VGroup(VGroup(Q1))))
        
        nah1 = TexMobject("R","=0").scale_to_fit_height(0.4).next_to(pop, 0.1*DOWN+12*LEFT)
        nah1[0].set_color(ORANGE)
        nah2 = nah1.deepcopy().shift(2*RIGHT+2*UP)
        nah3 = nah1.deepcopy().shift(2*RIGHT+2*DOWN)
        self.wait()

        for stuff in [nah1, nah2, nah3]:
            self.play(Write(stuff), run_time = 0.15)
        self.wait()
            
        Q01 = TexMobject("Q","(","s",",","a",")=","0").next_to(arrows[0], UP)
        Q01.set_color_by_tex_to_color_map({       
                    "Q":MAROON,
                    "s":TEAL_E,
                    "a":YELLOW,                  
                    "R":ORANGE,
                    "pha":PURPLE_A,
                    "\gamma":PURPLE_D,
                    "max":MAROON,
                    "1":GREEN,
                    "-":RED,
                    "0":DARK_GRAY
                    })
        Q02 = Q01.deepcopy().next_to(arrows[2], DOWN)
        Q03 = Q01.deepcopy().next_to(arrows[3], LEFT)
        self.play(FadeInFromDown(Q01),
                  FadeInFromDown(Q02),
                  FadeInFromDown(Q03))
        self.wait()
        
        mousy.shift(2*LEFT)
        self.play(FadeIn(mousy))
        rttttt = TextMobject(
                "I ",
                "should ",
                "go right",
                "!")
        rttttt[0].set_color(GRAY)
        rttttt[2].set_color(YELLOW)

        self.wait()               
        self.play(PiCreatureSays(
                mousy, rttttt,    
                target_mode = "surprised",))
        arrows[1].set_color(YELLOW)
        self.play(GrowFromPoint(arrows[1], arrows[1].get_start()), run_time = RUSH_RUNTIME)
        self.wait() # 5 so we build an AI?
        
# limitation
        self.play(RemovePiCreatureBubble(mousy))
        self.remove(arrows)
        arrows[1].set_color(WHITE)
        for stuff in [mousy, Q1, Q01, Q02, Q03, nah1, nah2, nah3]:
            self.remove(stuff)
        mousy.shift(2*LEFT)
        arrows[0].next_to(mousy, UP)
        arrows[1].next_to(mousy, RIGHT)
        arrows[2].next_to(mousy, DOWN)
        arrows[3].next_to(mousy, LEFT)
        
        self.add(D2)
        self.play(FadeIn(mousy),
                  GrowFromPoint(arrows[0], arrows[0].get_start()),
                  GrowFromPoint(arrows[1], arrows[1].get_start()),
                  GrowFromPoint(arrows[2], arrows[2].get_start()),
                  GrowFromPoint(arrows[3], arrows[3].get_start()))
        self.remove(D2)
        
        nah1 = TexMobject("R","=0").scale_to_fit_height(0.4).next_to(pop, 0.1*DOWN+20*LEFT)
        nah1[0].set_color(ORANGE)
        nah2 = nah1.deepcopy().shift(2*RIGHT+2*UP)
        nah3 = nah1.deepcopy().shift(2*RIGHT+2*DOWN)
        nah4 = nah1.deepcopy().shift(4*RIGHT)
        for stuff in[nah2, nah4, nah3, nah1]:
            self.play(FadeIn(stuff), run_time = RUSH_RUNTIME)
        for stuff in[nah2, nah4, nah3, nah1]:
            self.play(FadeOut(stuff), run_time = RUSH_RUNTIME)

        Q01 = TexMobject("Q","(","s",",","a",")=","0").next_to(arrows[0], UP)
        Q01.set_color_by_tex_to_color_map({       
                    "Q":MAROON,
                    "s":TEAL_E,
                    "a":YELLOW,                  
                    "R":ORANGE,
                    "pha":PURPLE_A,
                    "\gamma":PURPLE_D,
                    "max":MAROON,
                    "1":GREEN,
                    "-":RED,
                    "0":DARK_GRAY
                    })
        Q02 = Q01.deepcopy().next_to(arrows[2], DOWN)
        Q03 = Q01.deepcopy().next_to(arrows[3], LEFT)
        Q04 = Q01.deepcopy().next_to(arrows[1], RIGHT)
        for stuff in[Q01, Q04, Q02, Q03]:
            self.play(FadeInFromDown(stuff), run_time = 0.1)

        foo = TextMobject(
                "Where ",
                "should ",
                "I ",
                "go"
                "!?")
        foo[2].set_color(GRAY)
        self.wait()
        self.play(PiCreatureSays(
                mousy, foo,    
                target_mode = "angry",))
        self.wait()
        
        self.play(RemovePiCreatureBubble(mousy))
        for stuff in [arrows, Q04, Q01, Q02, Q03, nah1, nah2, nah3, nah4, QR_expr, rect]:
            self.remove(stuff)
        self.play(FadeOut(arrows),
                  FadeOut(rect),
                  FadeOut(QR_expr))       
        
        arrows[1].set_color(YELLOW)
        self.play(GrowFromPoint(arrows[1], arrows[1].get_start()), run_time = RUSH_RUNTIME)
        for right in [2*RIGHT]:
            self.play(ApplyMethod(mousy.shift, right, run_time = 1))
        self.remove(arrows[1])
        arrows[1].set_color(WHITE)
        arrows[0].next_to(mousy, UP)
        arrows[1].next_to(mousy, RIGHT)
        arrows[2].next_to(mousy, DOWN)
        arrows[3].next_to(mousy, LEFT)
        
        self.play(GrowFromPoint(arrows[0], arrows[0].get_start()),
                  GrowFromPoint(arrows[1], arrows[1].get_start()),
                  GrowFromPoint(arrows[2], arrows[2].get_start()),
                  GrowFromPoint(arrows[3], arrows[3].get_start()))    
        self.play(PiCreatureSays(
                mousy, "Why!?",    
                target_mode = "confused",))        
        hmm = TextMobject(
            "After taking the ","action ","to ","go right \\\\ ",
            "there is a chance to take an ","action \\\\ ",
            "with a super high","Q","(","s",",","a",")"
        ).to_corner(DOWN).scale_to_fit_width(12)
        hmm.set_color_by_tex_to_color_map({        
                "function":MAROON,
                "quality":MAROON,
                "action":YELLOW,
                "state":TEAL_E,
                })  
        hmm[-2].set_color(YELLOW)
        hmm[-4].set_color(TEAL_E)
        hmm[-6].set_color(MAROON)
        self.wait()
        
        self.remove(arrows[0])
        self.remove(arrows[1])
        self.remove(arrows[2])
        self.remove(arrows[3])
        
        self.play(RemovePiCreatureBubble(mousy), run_time = RUSH_RUNTIME)
        self.play(FadeOut(mousy), run_time = RUSH_RUNTIME)
        mousy.shift(2*LEFT)            
        self.play(FadeIn(mousy), run_time = RUSH_RUNTIME)
        self.play(Write(hmm), run_time = 4)
        arrows[0].next_to(mousy, UP)
        arrows[1].next_to(mousy, RIGHT)
        arrows[2].next_to(mousy, DOWN)
        arrows[3].next_to(mousy, LEFT)

        self.play(GrowFromPoint(arrows[0], arrows[0].get_start()),
                  GrowFromPoint(arrows[1], arrows[1].get_start()),
                  GrowFromPoint(arrows[2], arrows[2].get_start()),
                  GrowFromPoint(arrows[3], arrows[3].get_start()))       
        self.play(ReplacementTransform(
                VGroup(arrows[0]),
                VGroup(arrows[1])),
        ReplacementTransform(
                VGroup(arrows[2]),
                VGroup(arrows[1])),
        ReplacementTransform(
                VGroup(arrows[3]),
                VGroup(arrows[1]))
                )

        arrows[1].set_color(YELLOW)
        self.play(DrawBorderThenFill(arrows[1]), run_time = RUSH_RUNTIME)
        for right in [2*RIGHT]:
            self.play(ApplyMethod(mousy.shift, right, run_time = 1))
        
        self.remove(arrows[1])
        arrows[1].set_color(WHITE)
        arrows = VMobject(Vector([0, 1]).set_color(WHITE), 
                          Vector([1, 0]).set_color(YELLOW),
                          Vector([0, -1]).set_color(WHITE), 
                          Vector([-1, 0]).set_color(WHITE)
                          )
        arrows.scale(0.7)
        arrows[0].next_to(mousy, UP)
        arrows[1].next_to(mousy, RIGHT)
        arrows[2].next_to(mousy, DOWN)
        arrows[3].next_to(mousy, LEFT)
        
        Q01 = TexMobject("Q","(","s",",","a",")=","0").next_to(arrows[0], UP)
        Q01.set_color_by_tex_to_color_map({       
                    "Q":MAROON,
                    "s":TEAL_E,
                    "a":YELLOW,                  
                    "R":ORANGE,
                    "pha":PURPLE_A,
                    "\gamma":PURPLE_D,
                    "max":MAROON,
                    "1":GREEN,
                    "-":RED,
                    "0":DARK_GRAY
                    })
        Q02 = Q01.deepcopy().next_to(arrows[2], DOWN)
        Q03 = Q01.deepcopy().next_to(arrows[3], LEFT)
        Q04 = TexMobject("Q","(","s",",","a",")=","1").next_to(arrows[1], RIGHT)
        Q04.set_color_by_tex_to_color_map({       
                    "Q":MAROON,
                    "s":TEAL_E,
                    "a":YELLOW,                  
                    "R":ORANGE,
                    "pha":PURPLE_A,
                    "\gamma":PURPLE_D,
                    "max":MAROON,
                    "1":GREEN,
                    "-":RED,
                    "0":DARK_GRAY
                    })        
        
        self.play(GrowFromPoint(arrows[0], arrows[0].get_start()),
                  GrowFromPoint(arrows[1], arrows[1].get_start()),
                  GrowFromPoint(arrows[2], arrows[2].get_start()),
                  GrowFromPoint(arrows[3], arrows[3].get_start())) 
        arrows[1].set_color(YELLOW)
        self.play(DrawBorderThenFill(arrows[1]), run_time = RUSH_RUNTIME)

        self.play(FadeInFromDown(Q01),
                  FadeInFromDown(Q02),
                  FadeInFromDown(Q03),
                  FadeInFromDown(Q04))
        rect = SurroundingRectangle(Q04)
        self.play(ShowCreation(rect))
        self.wait()
        
        self.play(ReplacementTransform(
                VGroup(arrows[0]),
                VGroup(arrows[1])),
        ReplacementTransform(
                VGroup(arrows[2]),
                VGroup(arrows[1])),
        ReplacementTransform(
                VGroup(arrows[3]),
                VGroup(arrows[1]))
                )
        self.play(FadeOut(Q01),
                  FadeOut(Q02),
                  FadeOut(Q03),
                  FadeOut(Q04),
                  FadeOut(rect),
                  run_time = RUSH_RUNTIME)
        
        for right in [2*RIGHT]:
            self.play(ApplyMethod(mousy.shift, right, run_time = 1))        
        
        self.wait()
        


#####################
class FutureReward(TeacherStudentsScene):
    def construct(self):
       self.meow()

    def meow(self):
        suggestion_t = TextMobject(
            "So we should take future ","reward","into account"
        )
        suggestion_t.set_color_by_tex_to_color_map({        # This method is so awful to use 
                "function":MAROON,
                "quality":MAROON,
                "action":YELLOW,
                "state":TEAL_E
                })  

        self.teacher_says(
                suggestion_t,
                run_time = 3
                )
        self.change_student_modes(
                "pondring",
                "happy",
                "raise_right_hand"
                )
        self.wait()
#########################
        
QRQ_name = TextMobject(
            "We need to care about future","reward")
QRQ_name[1].set_color(YELLOW)

QRQ_expr = TexMobject(
"Q","(","s",",","a",") = ","R","+","\\gamma","\\max","_{a}","Q","(","s'",",","a",")",
                              alignment = '').scale_to_fit_width(12)
QRQ_expr2 = TexMobject(
"Q","(","s",",","a",") = ","R","+","0.9","\\max","_{a}","Q","(","s'",",","a",")",
                              alignment = '').scale_to_fit_width(12).scale(0.8).to_corner(UP+RIGHT)
QRQ_expr3 = TexMobject(
"Q","(","s",",","a",") = ","0","+","0.9","\\max","_{a}","Q","(","s'",",","a",")",
                              alignment = '').scale_to_fit_width(12).scale(0.8).to_corner(UP+RIGHT)
QRQ_expr4 = TexMobject(
"Q","(","s",",","a",") = ","0","+","0.9","\\times","1"," "," "," "," "," "," ",
                              alignment = '').scale_to_fit_width(12).scale(0.8).to_corner(UP+RIGHT)

QRQ_copy = QRQ_expr.deepcopy().scale(0.8).to_corner(UP+RIGHT)

for stuff in[QRQ_expr, QRQ_expr2, QRQ_expr3, QRQ_expr4, QRQ_copy]:
    stuff.set_color_by_tex_to_color_map({       
                    "Q":MAROON,
                    "s":TEAL_E,
                    "a":YELLOW,                  
                    "R":ORANGE,
                    "pha":PURPLE_A,
                    "\gamma":PURPLE_D,
                    "max":MAROON,
                    "0":ORANGE,
                    "0.9":PURPLE_D,
                    "1":MAROON
                    })   
      
           
qsa =  QRQ_expr[0:6]
rew = QRQ_expr[6]
maxq = QRQ_expr[9:17]      
gam = QRQ_expr[8]      

fr = QRQ_expr[8:17]

   
            
############
class ManInBell2(LinearTransformationScene):
    CONFIG = {
        "include_background_plane" : False,
        "show_basis_vectors" : False,
        "include_foreground_plane": False
    }
       
    def construct(self):
        self.equation_name()
        self.show_equation()
        self.put_into_play()


    def equation_name(self):
        QRQ_name.to_corner(UP+LEFT)
        self.play(Write(QRQ_name), run_time = RUSH_RUNTIME)
        
    def show_equation(self):          
        self.play(Write(QRQ_expr), play_time = 1)

        brace = Brace(fr, UP, buff = SMALL_BUFF)
        text = brace.get_text(
            "Future reward",
            buff = SMALL_BUFF
        ).set_color(ORANGE)
        self.play(GrowFromCenter(brace),
            Write(text, run_time = RUSH_RUNTIME),
        )
        brace.add(text)                

        terms = TexMobject("\\gamma",":Discount\, Factor (0\\leq ","\\gamma"," \\leq 1)")
        terms.set_color_by_tex_to_color_map({       
                    "\alpha":PURPLE_A,
                    "\gamma":PURPLE_D,
                    })    
        terms.to_corner(DOWN+RIGHT)
        self.play(FadeIn(terms))       
        self.wait()

        self.play(FadeOut(terms),
                  FadeOut(QRQ_name),
                  FadeOut(brace),
                  FadeOut(text))
        
    def put_into_play(self):
        self.play(QRQ_expr.scale, 0.8,
                  QRQ_expr.to_corner, UP+RIGHT,
            )
        self.add_plane()
        self.add(QRQ_expr)
# ctrl+c & ctrl+v zone start
        mousy = Randolph().scale_to_fit_height(1)

        pop = SVGMobject(file_name = "lollipop").rotate(90)
        pop.scale_to_fit_height(1)
        pop.set_fill(GREEN_C)        

        fire = SVGMobject(file_name = "fire")
        fire.scale_to_fit_height(1)
        fire.set_fill(RED)
        fire_2 = fire.deepcopy()

        rb_1 = SVGMobject(file_name = "roadblock").rotate(135.08) 
        rb_1.scale_to_fit_height(1)
        rb_1.set_fill(DARK_GRAY)
        rb_2 = rb_1.deepcopy()
        rb_3 = rb_1.deepcopy()
        fw1 = rb_1.deepcopy() 
        fw2 = rb_1.deepcopy()
        fw3 = rb_1.deepcopy()
        
        pop.shift(4.9*RIGHT+UP)
        fire.shift(5*RIGHT+3*DOWN)  
        fire_2.shift(5*LEFT+1*UP)
        rb_1.shift(1*RIGHT+1*DOWN)         
        rb_2.shift(1*LEFT+3*UP)           
        rb_3.shift(3*LEFT+3*DOWN)
        fw1.shift(5*RIGHT+3*DOWN)
        fw2.shift(5*LEFT+1*UP)
        fw3.shift(4.9*RIGHT+UP)        
        mousy.shift(1*RIGHT+1*UP)
        
        fw1_lable = TexMobject("FireWall").scale_to_fit_height(0.2).move_to(fire).set_color(GREEN)
        fw2_lable = fw1_lable.deepcopy().move_to(fire_2)
        fw3_lable = TexMobject("NO\, POP").scale_to_fit_height(0.2).move_to(pop).set_color(RED)
        rect1 = SurroundingRectangle(fw1_lable).set_color(GREEN)
        rect2 = SurroundingRectangle(fw2_lable).set_color(GREEN)
        rect3 = SurroundingRectangle(fw3_lable).set_color(RED)
        
        fw1.add(fw1_lable)
        fw2.add(fw2_lable)
        fw3.add(fw3_lable)
        fw1.add(rect1)
        fw2.add(rect2)
        fw3.add(rect3)

        r_1 = TexMobject("R=+1").scale_to_fit_height(0.4).next_to(pop, 0.1*DOWN)
        r_2 = TexMobject("R=-1").scale_to_fit_height(0.4).next_to(fire, 0.2*DOWN)
        r_3 = TexMobject("R=-1").scale_to_fit_height(0.4).next_to(fire_2, 0.2*DOWN)
        for stuff in [r_1,r_2, r_3]:                   
            stuff[0].set_color(ORANGE)                                       
        r_1[2:4].set_color(GREEN)
        r_1[-1].set_color(GREEN)
        r_2[2:4].set_color(RED)
        r_2[-1].set_color(RED)
        r_3[2:4].set_color(RED)
        r_3[-1].set_color(RED)        
# ctrl+c & ctrl+v zone end   
        self.play(
                  FadeInFromDown(pop),
                  FadeInFromDown(fire),
                  FadeInFromDown(rb_1),
                  FadeInFromDown(rb_2),
                  FadeInFromDown(rb_3),
                  FadeInFromDown(fire_2),
                  FadeInFromDown(r_1),
                  FadeInFromDown(r_2),
                  FadeInFromDown(r_3),
                  FadeInFromDown(mousy)
                  )  
        self.add(QRQ_expr)
        rect = SurroundingRectangle(QRQ_expr)
        rect.set_color_by_gradient(RED, YELLOW)
        self.play(ShowCreation(rect))

# find path
        letgamma = TexMobject("Let","\\gamma","=0.9").shift(2*DOWN).scale(1.5)
        letgamma.set_color_by_tex_to_color_map({       
                    "\alpha":PURPLE_A,
                    "\gamma":PURPLE_D,
                    })    
        self.play(Write(letgamma),
                  DrawBorderThenFill(fw1),
                  DrawBorderThenFill(fw2))
        self.play(
                ReplacementTransform(
                VGroup(letgamma),
                VGroup(gam)),
                ReplacementTransform(
                VGroup(QRQ_expr),
                VGroup(QRQ_expr2))
                )
        
#        
        arrows = VMobject(Vector([0, 1]).set_color(WHITE), 
                          Vector([1, 0]).set_color(WHITE),
                          Vector([0, -1]).set_color(WHITE), 
                          Vector([-1, 0]).set_color(WHITE)
                          )
        arrows.scale(0.7)
        arrows[0].next_to(mousy, UP)
        arrows[1].next_to(mousy, RIGHT)
        arrows[2].next_to(mousy, DOWN)
        arrows[3].next_to(mousy, LEFT)
        
        Qeq = TexMobject("Q","(","s",",","a",")=","...").next_to(arrows[1], RIGHT)
        Qeq.set_color_by_tex_to_color_map({       
                    "Q":MAROON,
                    "s":TEAL_E,
                    "a":YELLOW,                  
                    "R":ORANGE,
                    "pha":PURPLE_A,
                    "\gamma":PURPLE_D,
                    "max":MAROON,
                    "1":GREEN,
                    "-":RED,
                    "0":DARK_GRAY
                    })
        Qeq2 = TexMobject("Q","(","s",",","a",")=","0.9").next_to(arrows[1], RIGHT)
        Qeq2.set_color_by_tex_to_color_map({       
                    "Q":MAROON,
                    "s":TEAL_E,
                    "a":YELLOW,                  
                    "R":ORANGE,
                    "pha":PURPLE_A,
                    "\gamma":PURPLE_D,
                    "max":MAROON,
                    "1":GREEN,
                    "-":RED,
                    "0.9":MAROON
                    })
        ans = Qeq[-1]
        
        self.play(Write(arrows[1]),
                  FadeInFromDown(Qeq),
                  run_time = SUPER_RUSH_RUNTIME)
        
        r00 = TexMobject("R","=0").scale_to_fit_height(0.4).next_to(pop, 0.1*DOWN+4*LEFT)
        r00[0].set_color(ORANGE)
        
        self.play(FadeIn(r00), run_time = SUPER_RUSH_RUNTIME)
        self.play(
                ReplacementTransform(
                VGroup(r00),
                VGroup(rew)),
                run_time = SUPER_RUSH_RUNTIME)
        self.remove(rew)
        self.play(
                ReplacementTransform(
                VGroup(QRQ_expr2),
                VGroup(QRQ_expr3)),
                run_time = SUPER_RUSH_RUNTIME)
        
        future_arrows =  arrows[1].deepcopy().shift(2*RIGHT).set_color(WHITE)
        future_arrows2 =  arrows[0].deepcopy().shift(2*RIGHT).set_color(WHITE)
        future_arrows3 =  arrows[2].deepcopy().shift(2*RIGHT).set_color(WHITE)
        future_arrows4 =  arrows[3].deepcopy().shift(2*RIGHT).set_color(WHITE)
        future_q = TexMobject("Q","(","s",",","a",")=","1").next_to(future_arrows, RIGHT)
        future_q.set_color_by_tex_to_color_map({       
                    "Q":MAROON,
                    "s":TEAL_E,
                    "a":YELLOW,                  
                    "R":ORANGE,
                    "pha":PURPLE_A,
                    "\gamma":PURPLE_D,
                    "max":MAROON,
                    "1":GREEN,
                    "-":RED,
                    "0":DARK_GRAY
                    })
        future_q2 = TexMobject("Q","(","s",",","a",")=","\\leq","1").next_to(future_arrows2, 0.8*RIGHT)
        future_q2.set_color_by_tex_to_color_map({       
                    "Q":MAROON,
                    "s":TEAL_E,
                    "a":YELLOW,                  
                    "R":ORANGE,
                    "pha":PURPLE_A,
                    "\gamma":PURPLE_D,
                    "max":MAROON,
                    "1":GREEN,
                    "-":RED,
                    "0":DARK_GRAY
                    })
        future_q3 = future_q2.deepcopy().next_to(future_arrows3, DOWN)
        future_q4 = future_q2.deepcopy().next_to(future_arrows4, LEFT)
        
        self.play(ApplyMethod(mousy.shift, 2*RIGHT, run_time = SUPER_RUSH_RUNTIME),
                  GrowFromPoint(future_arrows, future_arrows.get_start()),
                  GrowFromPoint(future_arrows2, future_arrows2.get_start()),
                  GrowFromPoint(future_arrows3, future_arrows3.get_start()),
                  GrowFromPoint(future_arrows4, future_arrows4.get_start()),
                  FadeInFromDown(future_q),
                  FadeInFromDown(future_q2),
                  FadeInFromDown(future_q3),
                  FadeInFromDown(future_q4),
                  run_time = SUPER_RUSH_RUNTIME)
        
        max_arrow = Arrow(rb_1.get_bottom(), future_q.get_bottom(), stroke_width = 1000)
        max_arrow.set_color(MAROON)
        max_label = TexMobject("MAX").set_color(MAROON).next_to(max_arrow, DOWN).shift(2*LEFT).scale(2)
        self.play(GrowFromPoint(max_arrow, max_arrow.get_start()),
                  Write(max_label),
                  run_time = SUPER_RUSH_RUNTIME)
        
        self.play(
                ReplacementTransform(
                VGroup(future_arrows2),
                VGroup(future_q)),
                ReplacementTransform(
                VGroup(future_arrows3),
                VGroup(future_q)),
                ReplacementTransform(
                VGroup(future_arrows4),
                VGroup(future_q)),
                ReplacementTransform(
                VGroup(future_q2),
                VGroup(future_q)),
                ReplacementTransform(
                VGroup(future_q3),
                VGroup(future_q)),
                ReplacementTransform(
                VGroup(future_q4),
                VGroup(future_q)),
                ReplacementTransform(
                VGroup(future_arrows),
                VGroup(future_q)),
                run_time = SUPER_RUSH_RUNTIME)       
        
        self.play(ReplacementTransform(
                VGroup(future_q),
                VGroup(maxq)),
                FadeOut(max_arrow),
                FadeOut(max_label),
                run_time = SUPER_RUSH_RUNTIME
                )
        self.remove(maxq)
        self.play(
                ReplacementTransform(
                VGroup(QRQ_expr3),
                VGroup(QRQ_expr4)),
                run_time = SUPER_RUSH_RUNTIME)
                
        
        arrows[1].set_color(YELLOW)
        self.play(DrawBorderThenFill(arrows[1]),
                  FadeInFromDown(Qeq),
                  run_time = SUPER_RUSH_RUNTIME)
        self.play(ReplacementTransform(
                VGroup(qsa),
                VGroup(ans)),
                ReplacementTransform(
                VGroup(Qeq),
                VGroup(Qeq2)),
                run_time = SUPER_RUSH_RUNTIME)
        self.wait(3) # 
#     
        self.remove(Qeq2)
        self.remove(QRQ_expr4)
        self.remove(arrows[1])
        self.play(DrawBorderThenFill(QRQ_copy),
                  Write(twar("r",1,1,0.9)),
                  FadeOut(mousy),
                  run_time = RUSH_RUNTIME
                  )
        QRQ_copy.add(rect)
        self.play(QRQ_copy.scale, 0.5,
                  QRQ_copy.to_corner, LEFT+UP,
            )
 
        self.play(Write(twar("r",2,1,1)),
                  Write(twar("u",2,0,0.9)),
                  run_time = SUPER_RUSH_RUNTIME)
        self.play(Write(twar("r",0,1,0.81)),
                  Write(twar("u",2,-1,0.81)),
                  run_time = SUPER_RUSH_RUNTIME)
        self.play(Write(twar("r",-1,1,0.729)),
                  Write(twar("r",1,-1,0.729)),
                  run_time = SUPER_RUSH_RUNTIME)
        
        mousy.shift(6*LEFT)
        self.play(FadeInFromDown(mousy),run_time = SUPER_RUSH_RUNTIME)
        self.play(DrawBorderThenFill(ar("r",-1,1,0.729).set_color(YELLOW).shift(SHIFT_CONSTANT*UP)),
                  run_time = SUPER_RUSH_RUNTIME)
        self.play(DrawBorderThenFill(ar("r",0,1,0.81).set_color(YELLOW).shift(SHIFT_CONSTANT*UP)),
                  run_time = SUPER_RUSH_RUNTIME)
        self.play(DrawBorderThenFill(ar("r",1,1,0.9).set_color(YELLOW).shift(SHIFT_CONSTANT*UP)),
                  run_time = SUPER_RUSH_RUNTIME)
        self.play(DrawBorderThenFill(ar("r",2,1,1).set_color(YELLOW).shift(SHIFT_CONSTANT*UP)),
                  run_time = SUPER_RUSH_RUNTIME)        

        self.play(Write(twar("r",-1,1,0.729)),
                  Write(twar("r",0,1,0.81)),
                  Write(twar("r",1,1,0.9)),
                  Write(twar("r",2,1,1)),
                  run_time = 0.001)
        for i in [4*DOWN+4*RIGHT]:
            self.play(ApplyMethod(mousy.shift, i, run_time = 0.5))     
        self.play(DrawBorderThenFill(ar("r",1,-1,0.729).set_color(YELLOW).shift(SHIFT_CONSTANT*UP)),
                  run_time = SUPER_RUSH_RUNTIME)
        self.play(DrawBorderThenFill(ar("u",2,-1,0.81).set_color(YELLOW).shift(SHIFT_CONSTANT*RIGHT)),
                  run_time = SUPER_RUSH_RUNTIME)
        self.play(DrawBorderThenFill(ar("u",2,0,0.9).set_color(YELLOW).shift(SHIFT_CONSTANT*RIGHT)),
                  run_time = SUPER_RUSH_RUNTIME)
        self.play(DrawBorderThenFill(ar("r",2,1,1).set_color(YELLOW).shift(SHIFT_CONSTANT*UP)),
                  run_time = SUPER_RUSH_RUNTIME)
        self.wait()
        
# ctrl+c & ctrl+v zone start
class ManInBell2_2(LinearTransformationScene):        #messy arrows
    CONFIG = {"include_background_plane" : False,
        "show_basis_vectors" : False,
        "include_foreground_plane": False}       
    def construct(self):
        self.put_into_play()
    def put_into_play(self):
        QRQ_expr.scale(0.8).to_corner(UP+RIGHT).scale(0.5).to_corner(LEFT+UP)
        self.add_plane()
        self.add(QRQ_expr)
        mousy = Randolph().scale_to_fit_height(1)
        pop = SVGMobject(file_name = "lollipop").rotate(90)
        pop.scale_to_fit_height(1)
        pop.set_fill(GREEN_C)        
        fire = SVGMobject(file_name = "fire")
        fire.scale_to_fit_height(1)
        fire.set_fill(RED)
        fire_2 = fire.deepcopy()
        rb_1 = SVGMobject(file_name = "roadblock").rotate(135.08) 
        rb_1.scale_to_fit_height(1)
        rb_1.set_fill(DARK_GRAY)
        rb_2 = rb_1.deepcopy()
        rb_3 = rb_1.deepcopy()
        fw1 = rb_1.deepcopy() 
        fw2 = rb_1.deepcopy()
        fw3 = rb_1.deepcopy()        
        pop.shift(4.9*RIGHT+UP)
        fire.shift(5*RIGHT+3*DOWN)  
        fire_2.shift(5*LEFT+1*UP)
        rb_1.shift(1*RIGHT+1*DOWN)         
        rb_2.shift(1*LEFT+3*UP)           
        rb_3.shift(3*LEFT+3*DOWN)
        fw1.shift(5*RIGHT+3*DOWN)
        fw2.shift(5*LEFT+1*UP)
        fw3.shift(4.9*RIGHT+UP)        
        mousy.shift(1*RIGHT+1*UP)       
        fw1_lable = TexMobject("FireWall").scale_to_fit_height(0.2).move_to(fire).set_color(GREEN)
        fw2_lable = fw1_lable.deepcopy().move_to(fire_2)
        fw3_lable = TexMobject("NO\, POP").scale_to_fit_height(0.2).move_to(pop).set_color(RED)
        rect1 = SurroundingRectangle(fw1_lable).set_color(GREEN)
        rect2 = SurroundingRectangle(fw2_lable).set_color(GREEN)
        rect3 = SurroundingRectangle(fw3_lable).set_color(RED)        
        fw1.add(fw1_lable)
        fw2.add(fw2_lable)
        fw3.add(fw3_lable)
        fw1.add(rect1)
        fw2.add(rect2)
        fw3.add(rect3)
        r_1 = TexMobject("R=+1").scale_to_fit_height(0.4).next_to(pop, 0.1*DOWN)
        r_2 = TexMobject("R=-1").scale_to_fit_height(0.4).next_to(fire, 0.2*DOWN)
        r_3 = TexMobject("R=-1").scale_to_fit_height(0.4).next_to(fire_2, 0.2*DOWN)
        for stuff in [r_1,r_2, r_3]:                   
            stuff[0].set_color(ORANGE)                                       
        r_1[2:4].set_color(GREEN)
        r_1[-1].set_color(GREEN)
        r_2[2:4].set_color(RED)
        r_2[-1].set_color(RED)
        r_3[2:4].set_color(RED)
        r_3[-1].set_color(RED)        
        rect = SurroundingRectangle(QRQ_expr)
        rect.set_color_by_gradient(RED, YELLOW)
        QRQ_copy.add(rect)
        for stuff in[mousy, pop, fire, fire_2, rb_1, rb_2, rb_3, r_1, r_2, r_3, QRQ_expr, rect]:
            self.add(stuff)
        pop_rad = AmbientLight(
                    num_levels= 200, 
                    radius= 15,
                    max_opacit= 0.2,
                    color= GREEN,
                    opacity_function = inverse_power_law(1, 1, 1, 1.3)
                    ).shift(UP+5*RIGHT)
        fire_rad = AmbientLight(
                num_levels= 200,
                radius= 15,
                max_opacit= 0.2,
                color= RED,
                opacity_function = inverse_power_law(1, 1, 1, 1.3)
                    ).shift(4*DOWN)
        fire_rad_2 = AmbientLight(
                num_levels= 200,
                radius= 15,
                max_opacit= 0.2,
                color= RED,
                opacity_function = inverse_power_law(1, 1, 1, 1.3)
                    ).shift(10*LEFT+4*UP)
# ctrl+c & ctrl+v zone end
        mousy.shift(4*DOWN+2*RIGHT)
        self.add(fw1)
        self.add(fw2)
        self.play(Write(twar("u",3,0,1)),
                  Write(twar("r",2,1,1)),
                  Write(twar("d",3,2,1)),
                  run_time = RUSH_RUNTIME)
        
        self.play(Write(twar("u",2,0,0.9)),
                  Write(twar("d",2,2,0.9)),                          # This is what happen if you're stupid
                  Write(twar("r",2,2,0.9)),
                  Write(twar("r",2,0,0.9)),
                  Write(twar("r",1,1,0.9)),
                  run_time = RUSH_RUNTIME)        
        
        self.play(Write(twar("u",2,-1,0.81)),
                  Write(ar("l",2,0,0.81)),
                  Write(twar("r",0,1,0.81)),
                  Write(twar("d",1,2,0.81)),                       
                  Write(twar("r",1,2,0.81)),
                  Write(ar("d",1,1,0.81)),
                  run_time = RUSH_RUNTIME)
        
        self.play(Write(twar("r",1,-1,0.729)),
                  Write(twar("u",0,0,0.729)),
                  Write(ar("u",0,1,0.729)),
                  Write(twar("r",-1,1,0.729)),
                  Write(ar("l",1,2,0.729)),
                  run_time = RUSH_RUNTIME)
        
        self.play(Write(twar("r",0,-1,0.6561)),
                  Write(twar("u",0,-1,0.6561)),
                  Write(twar("u",-1,0,0.6561)),
                  Write(twar("r",-1,0,0.6561)),
                  Write(ar("r",0,0,0.6561)),
                  Write(twar("d",-1,2,0.6561)),
                  Write(ar("u",1,-1,0.6561)),
                  run_time = RUSH_RUNTIME)
        self.wait()
        self.play(PiCreatureSays(
                mousy, "Leave this to computer!",    
                target_mode = "angry",
                play_time = 3
                ))
        self.wait(5)
         
# ctrl+c & ctrl+v zone start
class ManInBell2_3(LinearTransformationScene):          #fire
    CONFIG = {"include_background_plane" : False,
        "show_basis_vectors" : False,
        "include_foreground_plane": False}       
    def construct(self):
        self.put_into_play()
    def put_into_play(self):
        QRQ_expr.scale(0.8).to_corner(UP+RIGHT).scale(0.5).to_corner(LEFT+UP)
        self.add_plane()
        self.add(QRQ_expr)
        mousy = Randolph().scale_to_fit_height(1)
        pop = SVGMobject(file_name = "lollipop").rotate(90)
        pop.scale_to_fit_height(1)
        pop.set_fill(GREEN_C)        
        fire = SVGMobject(file_name = "fire")
        fire.scale_to_fit_height(1)
        fire.set_fill(RED)
        fire_2 = fire.deepcopy()
        rb_1 = SVGMobject(file_name = "roadblock").rotate(135.08) 
        rb_1.scale_to_fit_height(1)
        rb_1.set_fill(DARK_GRAY)
        rb_2 = rb_1.deepcopy()
        rb_3 = rb_1.deepcopy()
        fw1 = rb_1.deepcopy() 
        fw2 = rb_1.deepcopy()
        fw3 = rb_1.deepcopy()        
        pop.shift(4.9*RIGHT+UP)
        fire.shift(5*RIGHT+3*DOWN)  
        fire_2.shift(5*LEFT+1*UP)
        rb_1.shift(1*RIGHT+1*DOWN)         
        rb_2.shift(1*LEFT+3*UP)           
        rb_3.shift(3*LEFT+3*DOWN)
        fw1.shift(5*RIGHT+3*DOWN)
        fw2.shift(5*LEFT+1*UP)
        fw3.shift(4.9*RIGHT+UP)        
        mousy.shift(1*RIGHT+1*UP)       
        fw1_lable = TexMobject("FireWall").scale_to_fit_height(0.2).move_to(fire).set_color(GREEN)
        fw2_lable = fw1_lable.deepcopy().move_to(fire_2)
        fw3_lable = TexMobject("NO\, POP").scale_to_fit_height(0.2).move_to(pop).set_color(RED).shift(0.1*LEFT)
        rect1 = SurroundingRectangle(fw1_lable).set_color(GREEN)
        rect2 = SurroundingRectangle(fw2_lable).set_color(GREEN)
        rect3 = SurroundingRectangle(fw3_lable).set_color(RED)        
        fw1.add(fw1_lable)
        fw2.add(fw2_lable)
        fw3.add(fw3_lable)
        fw1.add(rect1)
        fw2.add(rect2)
        fw3.add(rect3)
        r_1 = TexMobject("R=+1").scale_to_fit_height(0.4).next_to(pop, 0.1*DOWN)
        r_2 = TexMobject("R=-1").scale_to_fit_height(0.4).next_to(fire, 0.2*DOWN)
        r_3 = TexMobject("R=-1").scale_to_fit_height(0.4).next_to(fire_2, 0.2*DOWN)
        for stuff in [r_1,r_2, r_3]:                   
            stuff[0].set_color(ORANGE)                                       
        r_1[2:4].set_color(GREEN)
        r_1[-1].set_color(GREEN)
        r_2[2:4].set_color(RED)
        r_2[-1].set_color(RED)
        r_3[2:4].set_color(RED)
        r_3[-1].set_color(RED)        
        rect = SurroundingRectangle(QRQ_expr)
        rect.set_color_by_gradient(RED, YELLOW)
        QRQ_copy.add(rect)
        for stuff in[mousy, pop, fire, fire_2, rb_1, rb_2, rb_3, r_1, r_2, r_3, QRQ_expr, rect]:
            self.add(stuff)
        pop_rad = AmbientLight(
                    num_levels= 200, 
                    radius= 15,
                    max_opacit= 0.2,
                    color= GREEN,
                    opacity_function = inverse_power_law(1, 1, 1, 1.3)
                    ).shift(UP+5*RIGHT)
        fire_rad = AmbientLight(
                num_levels= 200,
                radius= 15,
                max_opacit= 0.2,
                color= RED,
                opacity_function = inverse_power_law(1, 1, 1, 1.3)
                    ).shift(4*DOWN)
        fire_rad_2 = AmbientLight(
                num_levels= 200,
                radius= 15,
                max_opacit= 0.2,
                color= RED,
                opacity_function = inverse_power_law(1, 1, 1, 1.3)
                    ).shift(10*LEFT+4*UP)
# ctrl+c & ctrl+v zone end
        mousy.shift(+4*DOWN)
        for i in [2*RIGHT]:
            self.play(ApplyMethod(mousy.shift, i, run_time = RUSH_RUNTIME))       
        self.play(Write(twar("l",3,-1,-0.9)),
                  DrawBorderThenFill(fw3),
                  DrawBorderThenFill(fw2),
                  run_time = RUSH_RUNTIME)
        self.play(Write(twar("l",2,-1,-0.81)),run_time = SUPER_RUSH_RUNTIME)
        self.play(Write(twar("l",1,-1,-0.729)),run_time = SUPER_RUSH_RUNTIME)
        self.play(Write(twar("u",0,-1,-0.-0.6561)),run_time = SUPER_RUSH_RUNTIME)
        self.play(DrawBorderThenFill(ar("l",3,-1,-0.9).set_color(YELLOW).shift(SHIFT_CONSTANT*DOWN)),
                  run_time = SUPER_RUSH_RUNTIME)
        self.play(DrawBorderThenFill(ar("l",2,-1,-0.81).set_color(YELLOW).shift(SHIFT_CONSTANT*DOWN)),
                  run_time = SUPER_RUSH_RUNTIME)
        self.play(DrawBorderThenFill(ar("l",1,-1,-0.729).set_color(YELLOW).shift(SHIFT_CONSTANT*DOWN)),
                  run_time = SUPER_RUSH_RUNTIME)
        self.play(DrawBorderThenFill(ar("u",0,-1,-0.6561).set_color(YELLOW).shift(SHIFT_CONSTANT*RIGHT)),
                  run_time = SUPER_RUSH_RUNTIME)
        self.wait(2)
        
# ctrl+c & ctrl+v zone start
class ManInBell2_4(LinearTransformationScene):                       #radiation
    CONFIG = {"include_background_plane" : False,
        "show_basis_vectors" : False,
        "include_foreground_plane": False}       
    def construct(self):
        self.put_into_play()
    def put_into_play(self):
        QRQ_expr.scale(0.8).to_corner(UP+RIGHT).scale(0.5).to_corner(LEFT+UP)
        self.add_plane()
        self.add(QRQ_expr)
        mousy = Randolph().scale_to_fit_height(1)
        pop = SVGMobject(file_name = "lollipop").rotate(90)
        pop.scale_to_fit_height(1)
        pop.set_fill(GREEN_C)        
        fire = SVGMobject(file_name = "fire")
        fire.scale_to_fit_height(1)
        fire.set_fill(RED)
        fire_2 = fire.deepcopy()
        rb_1 = SVGMobject(file_name = "roadblock").rotate(135.08) 
        rb_1.scale_to_fit_height(1)
        rb_1.set_fill(DARK_GRAY)
        rb_2 = rb_1.deepcopy()
        rb_3 = rb_1.deepcopy()
        fw1 = rb_1.deepcopy() 
        fw2 = rb_1.deepcopy()
        fw3 = rb_1.deepcopy()        
        pop.shift(4.9*RIGHT+UP)
        fire.shift(5*RIGHT+3*DOWN)  
        fire_2.shift(5*LEFT+1*UP)
        rb_1.shift(1*RIGHT+1*DOWN)         
        rb_2.shift(1*LEFT+3*UP)           
        rb_3.shift(3*LEFT+3*DOWN)
        fw1.shift(5*RIGHT+3*DOWN)
        fw2.shift(5*LEFT+1*UP)
        fw3.shift(4.9*RIGHT+UP)        
        mousy.shift(3*LEFT+1*DOWN)       
        fw1_lable = TexMobject("FireWall").scale_to_fit_height(0.2).move_to(fire).set_color(GREEN)
        fw2_lable = fw1_lable.deepcopy().move_to(fire_2)
        fw3_lable = TexMobject("NO\, POP").scale_to_fit_height(0.2).move_to(pop).set_color(RED)
        rect1 = SurroundingRectangle(fw1_lable).set_color(GREEN)
        rect2 = SurroundingRectangle(fw2_lable).set_color(GREEN)
        rect3 = SurroundingRectangle(fw3_lable).set_color(RED)        
        fw1.add(fw1_lable)
        fw2.add(fw2_lable)
        fw3.add(fw3_lable)
        fw1.add(rect1)
        fw2.add(rect2)
        fw3.add(rect3)
        r_1 = TexMobject("R=+1").scale_to_fit_height(0.4).next_to(pop, 0.1*DOWN)
        r_2 = TexMobject("R=-1").scale_to_fit_height(0.4).next_to(fire, 0.2*DOWN)
        r_3 = TexMobject("R=-1").scale_to_fit_height(0.4).next_to(fire_2, 0.2*DOWN)
        for stuff in [r_1,r_2, r_3]:                   
            stuff[0].set_color(ORANGE)                                       
        r_1[2:4].set_color(GREEN)
        r_1[-1].set_color(GREEN)
        r_2[2:4].set_color(RED)
        r_2[-1].set_color(RED)
        r_3[2:4].set_color(RED)
        r_3[-1].set_color(RED)        
        rect = SurroundingRectangle(QRQ_expr)
        rect.set_color_by_gradient(RED, YELLOW)
        QRQ_copy.add(rect)
        for stuff in[pop, fire, fire_2, rb_1, rb_2, rb_3, r_1, r_2, r_3, QRQ_expr, rect]:
            self.add(stuff)
        pop_rad = AmbientLight(
                    num_levels= 200, 
                    radius= 15,
                    max_opacit= 0.2,
                    color= GREEN,
                    opacity_function = inverse_power_law(1, 1, 1, 1.3)
                    ).shift(UP+5*RIGHT)
        fire_rad = AmbientLight(
                num_levels= 200,
                radius= 15,
                max_opacit= 0.2,
                color= RED,
                opacity_function = inverse_power_law(1, 1, 1, 1.3)
                    ).shift(4*DOWN)
        fire_rad_power = AmbientLight(
                num_levels= 200,
                radius= 15,
                max_opacit= 0.2,
                color= RED,
                opacity_function = inverse_power_law(2, 1, 1.5, 2)
                    )
        fire_rad_2 = AmbientLight(
                num_levels= 200,
                radius= 15,
                max_opacit= 0.2,
                color= RED,
                opacity_function = inverse_power_law(1, 1, 1, 1.3)
                    ).shift(10*LEFT+4*UP)
# ctrl+c & ctrl+v zone end
        self.wait(5)
        
        self.play(SwitchOn(pop_rad),
                  SwitchOn(fire_rad),
                  SwitchOn(fire_rad_2),
                  play_time = 6
                  )                  
        self.wait()
        a1 = ar("r",-1,0).set_color(YELLOW)
        a2 = ar("u",0,0).set_color(YELLOW)
        a3 = ar("r",0,1).set_color(YELLOW)
        a4 = ar("r",1,1).set_color(YELLOW)
        a5 = ar("r",2,1).set_color(YELLOW)
        b1 = ar("l",1,-1).set_color(YELLOW)
        b2 = ar("u",0,-1).set_color(YELLOW)
        b3 = ar("l",0,0).set_color(YELLOW)
        b4 = ar("u",-1,0).set_color(YELLOW)
        b5 = ar("u",-1,1).set_color(YELLOW)
        b6 = ar("l",-1,2).set_color(YELLOW)
        
        
        self.play(FadeInFromDown(mousy))
        self.play(DrawBorderThenFill(a1),
                  run_time = SUPER_RUSH_RUNTIME)
        self.play(DrawBorderThenFill(a2),
                  run_time = SUPER_RUSH_RUNTIME)
        self.play(DrawBorderThenFill(a3),
                  run_time = SUPER_RUSH_RUNTIME)
        self.play(DrawBorderThenFill(a4),
                  run_time = SUPER_RUSH_RUNTIME)
        self.play(DrawBorderThenFill(a5),
                  run_time = SUPER_RUSH_RUNTIME)
        self.wait(2)
        self.remove(r_2)
        for stuff in [a1, a2, a3, a4, a5]:
            self.remove(stuff)
        
        r_power = TexMobject("R","=","-100").scale_to_fit_height(0.4).next_to(fire, 0.2*DOWN)
        r_power[0].set_color(ORANGE)
        r_power[-1].set_color(RED)
        
        rect = SurroundingRectangle(r_power)
        for i in [4*RIGHT+2*DOWN]:
            self.play(ApplyMethod(mousy.shift, i, run_time = 1),
                      ShowCreation(rect),
                      Write(r_power))
        self.play(SwitchOn(fire_rad_power))
        self.play(PiCreatureSays(
                mousy, "I'm not touching that!",    
                target_mode = "guilty",
                play_time = 1
                ))
        self.play(RemovePiCreatureBubble(mousy))
        
        self.play(DrawBorderThenFill(b1),
                  run_time = SUPER_RUSH_RUNTIME)
        self.play(DrawBorderThenFill(b2),
                  run_time = SUPER_RUSH_RUNTIME)
        self.play(DrawBorderThenFill(b3),
                  run_time = SUPER_RUSH_RUNTIME)
        self.play(DrawBorderThenFill(b4),
                  run_time = SUPER_RUSH_RUNTIME)
        self.play(DrawBorderThenFill(b5),
                  run_time = SUPER_RUSH_RUNTIME)
        self.play(DrawBorderThenFill(b6),
                  run_time = SUPER_RUSH_RUNTIME)
        self.wait()
        self.play(SwitchOff(fire_rad_power))
        self.wait(3)
        self.add(D3)
        self.wait()
        self.remove(D3)
        
        
                                     
  

##########################

alpha_equal = TexMobject("\\alpha","=","...").scale(2).shift(4*RIGHT+1.5*UP)
number_0 = TexMobject("\\alpha","=","0").scale(2).shift(4*RIGHT+1.5*UP)
number_1 = TexMobject("\\alpha","=","1").scale(2).shift(4*RIGHT+1.5*UP)

interpretation1 = TextMobject(
"Any reward the agent found \\\ ",
"immediately rewrite the value of Q(s, a)",
                             ).scale_to_fit_width(12).to_corner(UP
                                                 ).set_color_by_gradient(RED, BLUE)
interpretation2 = TextMobject(
"Keep using the old Q(s, a) value \\\ ",
"and ignoring any reward",
                              alignment = '').scale_to_fit_width(12).to_corner(UP
                                                                ).set_color_by_gradient(RED, BLUE)
    
bm_name = TextMobject("Bellman\, Equation"
                              ).scale_to_fit_width(12).set_color_by_gradient(RED, BLUE) 
bm_expr = TexMobject(
"Q_{new}","(","s",",","a",") = ","(1-","\\alpha",")","Q_{old}","(","s",",","a",")","+","\\alpha","[","R","+","\\gamma"," ","\\max","_{a}","Q","(","s'",",","a",")] ",
                              alignment = '').scale_to_fit_width(12)

bm_expr2 = TexMobject(
"Q_{new}","(","s",",","a",") = ","(1-","1",")","Q_{old}","(","s",",","a",")","+","1","[","R","+","\\gamma","\\max","_{a}","Q","(","s'",",","a",")] ",
                              alignment = '').scale_to_fit_width(12)
        
bm_expr3 = TexMobject(
"Q_{new}","(","s",",","a",") = ","R","+","\\gamma"," ","\\max","_{a}","Q","(","s'",",","a",")",
                              alignment = '').scale_to_fit_width(12)

bm_expr4 = TexMobject(
"Q_{new}","(","s",",","a",") = ","(1-","0",")","Q_{old}","(","s",",","a",")","+","0","[","R","+","\\gamma","\\max","_{a}","Q","(","s'",",","a",")] ",
                              alignment = '').scale_to_fit_width(12)

bm_expr5 = TexMobject(
"Q_{new}","(","s",",","a",") = ","Q_{old}","(","s",",","a",")",
                              alignment = '').scale_to_fit_width(12)

for stuff in [bm_expr, bm_expr2, bm_expr3, bm_expr4, bm_expr5]:  
    stuff.set_color_by_tex_to_color_map({       
                    "Q":MAROON,
                    "s":TEAL_E,
                    "a":YELLOW,                  
                    "R":ORANGE,
                    "pha":PURPLE_A,
                    "\gamma":PURPLE_D,
                    "max":MAROON,
                    "0":PURPLE_A,
                    }) 
for stuff in[alpha_equal, number_1, number_0]:
    stuff[0].set_color(PURPLE_A)
 
bm_expr2.set_color_by_tex_to_color_map({       
                    "1":PURPLE_A,
                    "(1-":WHITE
                    }) 
                    
bm_expr_copy = bm_expr.deepcopy()               # well...
bm_expr_copy2 = bm_expr.deepcopy()         


alp1 = bm_expr[7]
alp2 = bm_expr[16]
prev_q = bm_expr[6:15] 

hl1 = bm_expr2[16:29]
hl2 = bm_expr4[6:15]     

# ctrl+c & ctrl+v zone start
class EverChanging(LinearTransformationScene):                       #radiation
    CONFIG = {"include_background_plane" : False,
        "show_basis_vectors" : False,
        "include_foreground_plane": False}       
    def construct(self):
        self.put_into_play()
    def put_into_play(self):
        QRQ_expr.scale(0.8).to_corner(UP+RIGHT).scale(0.5).to_corner(LEFT+UP)
        self.add_plane()
        self.add(QRQ_expr)
        mousy = Randolph().scale_to_fit_height(1)
        pop = SVGMobject(file_name = "lollipop").rotate(90)
        pop.scale_to_fit_height(1)
        pop.set_fill(GREEN_C)        
        fire = SVGMobject(file_name = "fire")
        fire.scale_to_fit_height(1)
        fire.set_fill(RED)
        fire_2 = fire.deepcopy()
        rb_1 = SVGMobject(file_name = "roadblock").rotate(135.08) 
        rb_1.scale_to_fit_height(1)
        rb_1.set_fill(DARK_GRAY)
        rb_2 = rb_1.deepcopy()
        rb_3 = rb_1.deepcopy()
        fw1 = rb_1.deepcopy() 
        fw2 = rb_1.deepcopy()
        fw3 = rb_1.deepcopy()        
        pop.shift(4.9*RIGHT+UP)
        fire.shift(5*RIGHT+3*DOWN)  
        fire_2.shift(5*LEFT+1*UP)
        rb_1.shift(1*RIGHT+1*DOWN)         
        rb_2.shift(1*LEFT+3*UP)           
        rb_3.shift(3*LEFT+3*DOWN)
        fw1.shift(5*RIGHT+3*DOWN)
        fw2.shift(5*LEFT+1*UP)
        fw3.shift(4.9*RIGHT+UP)        
        mousy.shift(3*LEFT+1*DOWN)       
        fw1_lable = TexMobject("FireWall").scale_to_fit_height(0.2).move_to(fire).set_color(GREEN)
        fw2_lable = fw1_lable.deepcopy().move_to(fire_2)
        fw3_lable = TexMobject("NO\, POP").scale_to_fit_height(0.2).move_to(pop).set_color(RED)
        rect1 = SurroundingRectangle(fw1_lable).set_color(GREEN)
        rect2 = SurroundingRectangle(fw2_lable).set_color(GREEN)
        rect3 = SurroundingRectangle(fw3_lable).set_color(RED)        
        fw1.add(fw1_lable)
        fw2.add(fw2_lable)
        fw3.add(fw3_lable)
        fw1.add(rect1)
        fw2.add(rect2)
        fw3.add(rect3)
        r_1 = TexMobject("R=+1").scale_to_fit_height(0.4).next_to(pop, 0.1*DOWN)
        r_2 = TexMobject("R=-1").scale_to_fit_height(0.4).next_to(fire, 0.2*DOWN)
        r_3 = TexMobject("R=-1").scale_to_fit_height(0.4).next_to(fire_2, 0.2*DOWN)
        for stuff in [r_1,r_2, r_3]:                   
            stuff[0].set_color(ORANGE)                                       
        r_1[2:4].set_color(GREEN)
        r_1[-1].set_color(GREEN)
        r_2[2:4].set_color(RED)
        r_2[-1].set_color(RED)
        r_3[2:4].set_color(RED)
        r_3[-1].set_color(RED)        
        rect = SurroundingRectangle(QRQ_expr)
        rect.set_color_by_gradient(RED, YELLOW)
        QRQ_copy.add(rect)
        for stuff in[mousy, pop, fire, fire_2, rb_1, rb_2, rb_3, r_1, r_2, r_3]:
            self.add(stuff)
        pop_rad = AmbientLight(
                    num_levels= 200, 
                    radius= 15,
                    max_opacit= 0.2,
                    color= GREEN,
                    opacity_function = inverse_power_law(1, 1, 1, 1.3)
                    ).shift(UP+5*RIGHT)
        fire_rad = AmbientLight(
                num_levels= 200,
                radius= 15,
                max_opacit= 0.2,
                color= RED,
                opacity_function = inverse_power_law(1, 1, 1, 1.3)
                    ).shift(4*DOWN)
        fire_rad_power = AmbientLight(
                num_levels= 200,
                radius= 15,
                max_opacit= 0.2,
                color= RED,
                opacity_function = inverse_power_law(2, 1, 1.5, 2)
                    )
        fire_rad_2 = AmbientLight(
                num_levels= 200,
                radius= 15,
                max_opacit= 0.2,
                color= RED,
                opacity_function = inverse_power_law(1, 1, 1, 1.3)
                    ).shift(10*LEFT+4*UP)
# ctrl+c & ctrl+v zone end
        self.add(TextMobject("""Q-learning""").scale(4).to_corner(UP))
        self.wait(5)

class ManInBell3(LinearTransformationScene):
    CONFIG = {
        "include_background_plane" : False,
        "show_basis_vectors" : False,
        "include_foreground_plane": False
    }
       
    def construct(self):
        self.show_equation()
        
    def show_equation(self):                 
        terms = TexMobject("\\alpha",":Learning Rate (0\\leq ","\\alpha"," \\leq 1)\\\ ",
                           "\\gamma",":Discount Factor (0\\leq ","\\gamma"," \\leq 1)")
        terms.set_color_by_tex_to_color_map({       
                    "pha":PURPLE_A,
                    "\gamma":PURPLE_D,
                    })    
        terms.to_corner(DOWN+RIGHT)
        
        self.play(Write(bm_expr),
                  FadeIn(terms),
                  run_time = 1,)
        brace2 = Brace(alp1, UP, buff = SMALL_BUFF)
        text2 = brace2.get_text(
            "Learning rate",
            buff = SMALL_BUFF
        ).set_color(YELLOW).shift(1.6*RIGHT)  
        brace3 = Brace(alp2, UP, buff = SMALL_BUFF)

        self.play(GrowFromCenter(brace2),
                  GrowFromCenter(brace3),
                  Write(text2),
                  run_time = RUSH_RUNTIME
        ) 
        brace2.add(text2)               
        self.wait(2)

        self.remove(text2)
        self.play(FadeOut(brace2),
                  FadeOut(brace3),
                  run_time = SUPER_RUSH_RUNTIME)    
        
        brace = Brace(prev_q, UP, buff = SMALL_BUFF)
        text = brace.get_text(
            "Q(s,a) learned from previous experience",
            buff = SMALL_BUFF
        ).set_color(YELLOW)
        
        self.play(GrowFromCenter(brace),
            Write(text),
            run_time = RUSH_RUNTIME
        )
        brace.add(text)                
        self.wait(2)
        
        self.remove(text)
        self.play(FadeOut(brace), run_time = SUPER_RUSH_RUNTIME)    
        self.wait()

        self.play(Write(alpha_equal), run_time = SUPER_RUSH_RUNTIME)
        self.play(  ReplacementTransform(
                VGroup(alpha_equal),
                VGroup(number_1)),
                    ReplacementTransform(
                VGroup(bm_expr),
                VGroup(bm_expr2)),
                run_time = RUSH_RUNTIME)        
        rect = SurroundingRectangle(hl1)
        self.play(ShowCreation(rect))
        self.remove(rect)
        
        self.play(ReplacementTransform(
                VGroup(bm_expr2),
                VGroup(bm_expr3)),
                Write(interpretation1))
        self.wait(4) #
        self.remove(interpretation1)
        
        self.play(ReplacementTransform(
                VGroup(bm_expr3),
                VGroup(bm_expr_copy)))
        
        self.play(  ReplacementTransform(
                VGroup(number_1),
                VGroup(number_0)),
                    ReplacementTransform(
                VGroup(bm_expr_copy),
                VGroup(bm_expr4)),
                run_time = RUSH_RUNTIME)  
        rect = SurroundingRectangle(hl2)
        self.play(ShowCreation(rect))
        self.remove(rect)
        
        self.play(ReplacementTransform(
                VGroup(bm_expr4),
                VGroup(bm_expr5)),
                Write(interpretation2))
        self.wait(4) # 
        self.remove(interpretation2)
        
        self.play(ReplacementTransform(
                VGroup(bm_expr5),
                VGroup(bm_expr_copy2)),
                FadeOut(number_0))
        self.wait(2)
        
        bm_name.to_corner(UP+LEFT)
        self.play(Write(bm_name))
        self.play(Homotopy(plane_wave_homotopy, bm_name, run_time = 3))
        self.wait(10)
        
#        self.play(rate_func = there_and_back,
        
#############################################################################################
#####BORDER#####BORDER#####BORDER#####BORDER#####BORDER#####BORDER#####BORDER#####BORDER#####
#############################################################################################  

class LaboratoryMouse(PiCreature):
    CONFIG = {
            }

class Experiment(Scene):
    def construct(self):
        mousy = LaboratoryMouse().scale(2)
        self.play(
            FadeIn(mousy),
            Blink(mousy),
            )
        self.wait(5)
        self.play(Blink(mousy))
        self.wait(7)
        self.play(Blink(mousy))
        self.wait(3)
        
class OpeningQuote(Scene):
    def construct(self):
        words = TextMobject(
            "``The introduction of numbers as \\\\ coordinates is an act of violence.''",
        )
        words.to_edge(UP)    
        for mob in words.submobjects[27:27+11]:
            mob.set_color(GREEN)
        author = TextMobject("-Hermann Weyl")
        author.set_color(YELLOW)
        author.next_to(words, DOWN, buff = 0.5)

        self.play(FadeIn(words))
        self.wait(1)
        self.play(Write(author, run_time = 4))
        self.wait()

class ManInBell(LinearTransformationScene):
    CONFIG = {
        "include_background_plane" : False,
        "show_basis_vectors" : False,
        "include_foreground_plane": False
    }
       
    def construct(self):
        self.equation_name()
        self.show_equation()
        self.put_into_play()


    def equation_name(self):
        bm_name.to_corner(UP+LEFT)
        self.play(Write(bm_name))
        
    def show_equation(self):   
        bm_expression.set_color_by_tex_to_color_map({       
                    "Q":MAROON,
                    "s":TEAL_E,
                    "a":YELLOW,                  
                    "R":ORANGE,
                    "pha":PURPLE_A,
                    "\gamma":PURPLE_D,
                    "max":MAROON,
                    })          
        self.play(Write(bm_expression), play_time = 2)        

        terms = TexMobject("\\alpha",":Learning Rate\\\ ",
                           "\\gamma",":Discount Factor (0\\leq ","\\gamma"," \\leq 1)")
        terms.set_color_by_tex_to_color_map({       
                    "\alpha":PURPLE_A,
                    "\gamma":PURPLE_D,
                    })    
        terms.to_corner(DOWN+RIGHT)
        self.play(FadeIn(terms))
        
        self.wait()
#        self.play(rate_func = there_and_back,
        self.play(FadeOut(terms),
                  FadeOut(bm_name))
        
    def put_into_play(self):
        self.play(bm_expression.scale, 0.8,
                  bm_expression.to_corner, UP+RIGHT,
            )
        self.add_plane()
        self.add(bm_expression)
# ctrl+c & ctrl+v zone start
        mousy = Randolph().scale_to_fit_height(1)

        pop = SVGMobject(file_name = "lollipop").rotate(90)
        pop.scale_to_fit_height(1)
        pop.set_fill(GREEN_C)        

        fire = SVGMobject(file_name = "fire")
        fire.scale_to_fit_height(1)
        fire.set_fill(RED)
        fire_2 = fire.deepcopy()

        rb_1 = SVGMobject(file_name = "roadblock").rotate(135.08) 
        rb_1.scale_to_fit_height(1)
        rb_1.set_fill(DARK_GRAY)
        rb_2 = rb_1.deepcopy()
        rb_3 = rb_1.deepcopy()
        
        pop.shift(4.9*RIGHT+UP)
        fire.shift(5*RIGHT+3*DOWN)  
        fire_2.shift(5*LEFT+1*UP)
        rb_1.shift(1*RIGHT+1*DOWN)         
        rb_2.shift(1*LEFT+3*UP)           
        rb_3.shift(3*LEFT+3*DOWN)           
        mousy.shift(3*RIGHT+1*UP)

        r_1 = TexMobject("R=+1").scale_to_fit_height(0.4).next_to(pop, 0.1*DOWN)
        r_2 = TexMobject("R=-1").scale_to_fit_height(0.4).next_to(fire, 0.2*DOWN)
        r_3 = TexMobject("R=-1").scale_to_fit_height(0.4).next_to(fire_2, 0.2*DOWN)
        for stuff in [r_1,r_2, r_3]:                   
            stuff[0].set_color(ORANGE)                                       
        r_1[2:4].set_color(GREEN)
        r_1[-1].set_color(GREEN)
        r_2[2:4].set_color(RED)
        r_2[-1].set_color(RED)
        r_3[2:4].set_color(RED)
        r_3[-1].set_color(RED)        
# ctrl+c & ctrl+v zone end   
        self.play(
                  FadeInFromDown(pop),
                  FadeInFromDown(fire),
                  FadeInFromDown(rb_1),
                  FadeInFromDown(rb_2),
                  FadeInFromDown(rb_3),
                  FadeInFromDown(fire_2),
                  FadeInFromDown(r_1),
                  FadeInFromDown(r_2),
                  FadeInFromDown(r_3),
                  FadeInFromDown(mousy)
                  )  
        self.add(bm_expression)
        rect = SurroundingRectangle(bm_expression)
        self.play(ShowCreation(rect))

# find path
        reward_answer = TexMobject("The\, agent\, (randomly)\, decided\, to\, take\\\ a\, particular\, action\, (go\, right)\\\ while\, in\, a\, specific\, state\, (left\, to\, lollipop)").shift(2*DOWN).scale(1.5)
        reward_answer[3:8].set_color(GRAY)
        reward_answer[42:57].set_color(YELLOW)
        reward_answer[-21:-1].set_color(TEAL_E)
        reward_answer[-1].set_color(TEAL_E)
        self.play(Write(reward_answer))
        
        arrows = VMobject(Vector([0, 1]).set_color(WHITE), 
                          Vector([1, 0]).set_color(WHITE),
                          Vector([0, -1]).set_color(WHITE), 
                          Vector([-1, 0]).set_color(WHITE)
                          )
        arrows.scale(0.75)
        arrows[0].next_to(mousy, UP)
        arrows[1].next_to(mousy, RIGHT)
        arrows[2].next_to(mousy, DOWN)
        arrows[3].next_to(mousy, LEFT)
        self.play(Write(arrows))
        
        arrows[1].set_color(YELLOW)
        self.play(DrawBorderThenFill(arrows[1]), run_time = RUSH_RUNTIME)
        
        for right in [2*RIGHT]:
            self.play(ApplyMethod(mousy.shift, right, run_time = 1))
        eat = TexMobject("Reward = +1").next_to(mousy, UP+12*LEFT).scale(2)
        eat[0: 6].set_color(ORANGE)
        eat[7: 9].set_color(GREEN)
        pop_for_pi = SVGMobject(file_name = "lollipop").set_fill(GREEN_B).rotate(90).scale_to_fit_height(0.4)
        pop_for_pi.next_to(mousy, UP).shift(0.6*RIGHT+0.4*DOWN)
         
        self.play(mousy.change, "happy")
        self.play(DrawBorderThenFill(pop_for_pi),
                  Write(eat),
                  Blink(mousy))
        
# radiation
        pop_rad = AmbientLight(
                    num_levels= 200, 
                    radius= 15,
                    max_opacit= 0.2,
                    color= GREEN,
                    opacity_function = inverse_power_law(1, 1, 1, 1.3)
                    ).shift(UP+5*RIGHT)
        fire_rad = AmbientLight(
                num_levels= 200,
                radius= 15,
                max_opacit= 0.2,
                color= RED,
                opacity_function = inverse_power_law(1, 1, 1, 1.3)
                    ).shift(4*DOWN)
        fire_rad_2 = AmbientLight(
                num_levels= 200,
                radius= 15,
                max_opacit= 0.2,
                color= RED,
                opacity_function = inverse_power_law(1, 1, 1, 1.3)
                    ).shift(10*LEFT+4*UP)
        self.play(SwitchOn(pop_rad),
                  SwitchOn(fire_rad),
                  SwitchOn(fire_rad_2),
                  play_time = 6
                  )                  
        self.wait()
































