# Boids Algorithm

The Boids algorithm is a simulation developed by Craig Reynolds in 1986 to model the flocking behavior of birds. It's based on three simple rules that each boid (simulated bird) follows, resulting in complex collective behavior:

## Rules

### 1. Separation

Each boid steers to avoid crowding local flockmates. It maintains a minimum distance from its neighbors to prevent collisions and maintain personal space.

### 2. Alignment

Each boid adjusts its velocity to match that of its neighbors. This rule helps boids move in the same direction as the group, contributing to overall cohesion.

### 3. Cohesion

Each boid moves towards the average position of its neighbors. This rule promotes flocking behavior by pulling boids towards the center of the group.

## Implementation

The algorithm can be implemented as follows:

```pseudo
for each boid
    1. Compute the separation vector based on nearby boids.
    2. Compute the alignment vector based on nearby boids.
    3. Compute the cohesion vector based on nearby boids.
    4. Adjust the velocity of the boid based on weighted sums of the separation, alignment, and cohesion vectors.
    5. Update the position of the boid based on its velocity.
