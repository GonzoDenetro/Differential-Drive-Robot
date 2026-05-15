# Differential-Drive-Robot

A differential drive robot is a mobile robot controlled through two independent driving wheels.  
Each wheel can rotate at a different angular velocity, allowing the robot to perform:

- Forward and backward motion
- Rotation about its own axis
- Curved trajectories
- Path following

This project implements:

- Forward kinematics of a differential drive robot
- Euler integration
- Real-time simulation using Pygame
- Automatic square trajectory
- Automatic circular trajectory
- Manual keyboard control

---

# Kinematic Model

## Linear Velocity of the Robot

The total linear velocity of the robot is given by the average of the linear velocities of both wheels:

$$
V = \frac{V_r + V_l}{2}
$$

Where:

- \(V_r\): right wheel linear velocity
- \(V_l\): left wheel linear velocity

---

## Relationship Between Angular and Linear Velocity

The linear velocity of each wheel depends on:

- the wheel radius
- its angular velocity

\[
V_r = r \omega_r
\]

\[
V_l = r \omega_l
\]

Where:

- \(r\): wheel radius
- \(\omega_r\): right wheel angular velocity
- \(\omega_l\): left wheel angular velocity

---

## Velocity Components

The robot velocity can be decomposed into the \(x\) and \(y\) axes:

\[
\dot{x} = V \cos(\theta)
\]

\[
\dot{y} = V \sin(\theta)
\]

Substituting \(V\):

\[
\dot{x} = \left(\frac{r(\omega_r + \omega_l)}{2}\right)\cos(\theta)
\]

\[
\dot{y} = \left(\frac{r(\omega_r + \omega_l)}{2}\right)\sin(\theta)
\]

---

## Angular Velocity of the Robot

When the wheels rotate at different velocities, the robot rotates around a point called:

## Instantaneous Center of Rotation (ICR)

The angular velocity of the robot is given by:

\[
\omega = \frac{V_r - V_l}{L}
\]

Substituting the linear wheel velocities:

\[
\omega = \frac{r(\omega_r - \omega_l)}{L}
\]

Where:

- \(L\): distance between wheels

---

# Equations of Motion

The complete kinematic model of the differential drive robot is:

\[
\dot{x} = \left(\frac{r(\omega_r + \omega_l)}{2}\right)\cos(\theta)
\]

\[
\dot{y} = \left(\frac{r(\omega_r + \omega_l)}{2}\right)\sin(\theta)
\]

\[
\dot{\theta} = \frac{r(\omega_r - \omega_l)}{L}
\]

---

# Forward Kinematics

Forward kinematics consists of computing:

- position \(x\)
- position \(y\)
- orientation \(\theta\)

from the angular velocities of the wheels.

This project uses Euler numerical integration because the simulation works in discrete time.

---

# Euler Integration

The general Euler integration formula is:

\[
y_{n+1} = y_n + h f(t_n, y_n)
\]

Where:

- \(h\): step size
- \(f(t_n, y_n)\): system derivative

Applying Euler integration to the differential drive robot:

\[
x_{k+1} = x_k + \dot{x} \Delta t
\]

\[
y_{k+1} = y_k + \dot{y} \Delta t
\]

\[
\theta_{k+1} = \theta_k + \omega \Delta t
\]

---

# Code Implementation

The main forward kinematics function is:

```python
def forward_kinematics(phi_l, phi_r, x, y, theta, radius, L, dt):

    vel = ((phi_l * radius) + (phi_r * radius)) / 2

    omega = (radius * (-phi_l + phi_r)) / L

    x_dot = vel * math.cos(theta)
    y_dot = vel * math.sin(theta)

    x += x_dot * dt
    y += y_dot * dt
    theta += omega * dt

    return x, y, theta
```

---

# Controls

| Key | Action |
|---|---|
| ↑ | Move forward |
| ↓ | Move backward |
| → | Rotate |
| S | Square trajectory |
| C | Circular trajectory |

---

# Implemented Trajectories

## Square Trajectory

The square trajectory is implemented using:

1. Straight motion
2. Distance tracking
3. 90° rotation
4. Repetition of the process

A proportional controller is used for orientation control:

```python
omega_cmd = Kp * error
```

---

## Circular Trajectory

The circular trajectory uses the relation:

\[
R = \frac{V}{\omega}
\]

Given a desired radius and linear velocity, the required angular velocity is computed.

---

# Requirements

Install the required dependency:

```bash
pip install pygame
```

---

# Execution

Run the program:

```bash
python main.py
```

---

---

# Possible Improvements

- Implement inverse kinematics
- Add odometry
- Implement PID control
- Add simulated sensors
- Path planning
- More accurate physics simulation
