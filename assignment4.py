import numpy as np
from sim.sim2d_prediction import sim_run

# Simulator options.
options = {}
options['FIG_SIZE'] = [8,8]
options['ALLOW_SPEEDING'] = True

class KalmanFilter:
    def __init__(self):
        # Initial State
        self.x = np.matrix([[55.],
                            [3.],
                            [5.],
                            [0.]])

        # Uncertainity Matrix
        self.P = np.matrix([[0., 0., 0., 0.],
                            [0., 0., 0., 0.],
                            [0., 0., 0., 0.],
                            [0., 0., 0., 0.]])

        # Next State Function
        self.F = np.matrix([[1., 0., 0., 0.],
                            [0., 1., 0., 0.],
                            [0., 0., 1., 0.],
                            [0., 0., 0., 1.]])

        # Measurement Function
        self.H = np.matrix([[1, 0., 0., 0.],
                            [0., 1, 0., 0.]])

        # Measurement Uncertainty
        self.R = np.matrix([[0.01, 0.],
                            [0., 0.01]])
        # Identity Matrix
        self.I = np.matrix([[1., 0., 0., 0.],
                            [0., 1., 0., 0.],
                            [0., 0., 1., 0.],
                            [0., 0., 0., 1.]])
    def predict(self, dt):
        self.F[0, 2] = dt
        self.F[1, 3] = dt

        self.x = self.F * self.x
        self.P = self.F * self.P * np.transpose(self.F)

        return [self.x[0], self.x[1]]

    def measure_and_update(self,measurements, dt):
        self.F[0, 2] = dt
        self.F[1, 3] = dt

        z = np.matrix([measurements])
        y = np.transpose(z) - self.H * self.x
        s = self.H * self.P * np.transpose(self.H) + self.R
        k = self.P * np.transpose(self.H) * np.linalg.inv(s)
        self.x += k * y
        self.P = (self.I - k * self.H) * self.P

        self.P[0, 0] += 0.1
        self.P[1, 1] += 0.1
        self.P[2, 2] += 0.1
        self.P[3, 3] += 0.1

        return [self.x[0], self.x[1]]

    def predict_red_light(self,light_location):
        light_duration = 3
        F_new = np.copy(self.F)
        F_new[0,2] = light_duration
        F_new[1,3] = light_duration
        x_new = F_new * self.x
        if x_new[0] < light_location:
            return [False, x_new[0]]
        else:
            return [True, x_new[0]]

    def predict_red_light_speed(self, light_location):
        check = self.predict_red_light(light_location)
        if check[0]:
            return check
        light_duration = 3
        F_new = np.copy(self.F)
        F_new[0, 2] = 1
        F_new[1, 3] = 1
        x_new = F_new * self.x
        x_new[2] += 1.5

        F_new[0, 2] = light_duration - 1
        F_new[1, 3] = light_duration - 1
        x_new = F_new * x_new

        if x_new[0] < light_location:
            return [False, x_new[0]]
        else:
            return [True, x_new[0]]


for i in range(0,5):
    sim_run(options,KalmanFilter,i)
