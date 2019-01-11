import numpy as np
from sim.sim2d import sim_run

# Simulator options.
options = {}
options['FIG_SIZE'] = [8, 8]

options['DRIVE_IN_CIRCLE'] = True
# If False, measurements will be x,y.
# If True, measurements will be x,y, and current angle of the car.
# Required if you want to pass the driving in circle.
options['MEASURE_ANGLE'] = True
options['RECIEVE_INPUTS'] = True


class KalmanFilter:
    def __init__(self):
        # Initial State
        self.x = np.matrix([[0.],
                            [0.],
                            [0.],
                            [0.],
                            [0.]])

        # Uncertainty Matrix
        self.P = np.matrix([[100, 0., 0., 0., 0.],
                            [0., 100, 0., 0., 0.],
                            [0., 0., 100, 0., 0.],
                            [0., 0., 0., 100, 0.],
                            [0., 0., 0., 0., 100]])

        # Next State Function
        self.F = np.matrix([[1., 0., 0., 0., 0.],
                            [0., 1., 0., 0., 0.],
                            [0., 0., 1., 0., 0.],
                            [0., 0., 0., 1., 0.],
                            [0., 0., 0., 0., 1.]])

        # Measurement Function
        self.H = np.matrix([[1, 0., 0., 0., 0.],
                            [0., 1, 0., 0., 0.],
                            [0., 0, 0., 1., 0.]])

        # Measurement Uncertainty
        self.R = np.matrix([[0.01, 0., 0.],
                            [0., 0.01, 0.],
                            [0., 0., 0.01]])

        # Identity Matrix
        self.II = np.matrix([[1, 0., 0., 0., 0.],
                             [0., 1, 0., 0., 0.],
                             [0., 0., 1, 0., 0.],
                             [0., 0., 0., 1, 0.],
                             [0., 0., 0., 0., 1]])
        # Control Input
        self.u = np.matrix([[0.],
                            [0.]])

        # Control Matrix
        self.G = np.matrix([[0., 0.],
                            [0., 0.],
                            [1., 0.],
                            [0., 0.],
                            [0, 1.]])


    def predict(self, dt):
        self.F[0, 2] = dt
        self.F[1, 3] = dt
        self.F[3, 4] = dt

        self.x = self.F * self.x # + self.G * self.u
        self.P = self.F * self.P * np.transpose(self.F)

        return [self.x[0], self.x[1]]

    def measure_and_update(self, measurements, dt):
        self.F[0, 2] = dt
        self.F[1, 3] = dt
        self.F[3, 4] = dt

        z = np.matrix([measurements])
        y = np.transpose(z) - self.H * self.x
        s = self.H * self.P * np.transpose(self.H) + self.R
        k = self.P * np.transpose(self.H) * np.linalg.inv(s)
        self.x += k * y
        self.P = (self.II - k * self.H) * self.P

        self.P[0, 0] += 0.1
        self.P[1, 1] += 0.1
        self.P[2, 2] += 0.1
        self.P[3, 3] += 0.1

        return [self.x[0], self.x[1]]

    def recieve_inputs(self, u_steer, u_pedal):
        #self.u[0, 1] = u_steer
        #self.u[0, 0] = u_pedal

        return


sim_run(options, KalmanFilter)
