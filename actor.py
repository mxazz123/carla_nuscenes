import carla
class Actor:
    def __init__(self,scene,world,bp_name,location,rotation,options=None,attach_to=None):
        self.bp_name = bp_name
        self.world = world
        self.blueprint = world.get_blueprint_library().find(bp_name)
        if options is not None:
            for key in options:
                self.blueprint.set_attribute(key, options[key])
        self.transform = carla.Transform(carla.Location(**location),carla.Rotation(**rotation))
        self.attach_to = attach_to
        self.actor = None
        self.scene = scene

    def set_actor(self,id):
        self.actor = self.world.get_actor(id)

    def spawn_actor(self):
        self.actor = self.world.spawn_actor(self.blueprint,self.transform,self.attach_to)

    def get_actor(self):
        return self.actor

    def destroy(self):
        self.actor.destroy()

    def get_location(self):
        return self.actor.get_transform().transform(self.actor.bounding_box.location)

    def get_bbox(self):
        return self.actor.bounding_box.get_world_vertices(self.actor.get_transform())