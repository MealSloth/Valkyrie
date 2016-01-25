from abc import ABCMeta


class Gender(metaclass=ABCMeta):
    def __init__(self):
        pass

    MALE = 0
    FEMALE = 1
    OTHER = 2

    Gender = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    )


class PostStatus(metaclass=ABCMeta):
    def __init__(self):
        pass

    ACTIVE = 0
    SATURATED = 1
    INACTIVE = 2

    PostStatus = (
        (ACTIVE, 'Active'),
        (SATURATED, 'Saturated'),
        (INACTIVE, 'Inactive'),
    )


class OrderStatus(metaclass=ABCMeta):
    def __init__(self):
        pass

    PENDING = 0
    RECEIVED = 1
    PROGRESS = 2
    COMPLETED = 3
    SHIPPED = 4
    DELIVERED = 5
    DISPUTED = 6
    CANCELLED = 7

    OrderStatus = (
        (PENDING, 'Pending'),
        (RECEIVED, 'Received'),
        (PROGRESS, 'Progress'),
        (COMPLETED, 'Completed'),
        (SHIPPED, 'Shipped'),
        (DELIVERED, 'Delivered'),
        (DISPUTED, 'Disputed'),
        (CANCELLED, 'Cancelled'),
    )


class OrderType(metaclass=ABCMeta):
    def __init__(self):
        pass

    PICKUP = 0
    DELIVERY = 1
    DINEIN = 2

    OrderType = (
        (PICKUP, 'Pickup'),
        (DELIVERY, 'Delivery'),
        (DINEIN, 'DineIn'),
    )


class LocationPurpose(metaclass=ABCMeta):
    def __init__(self):
        pass

    BILLING = 0
    POST = 1
    DISPLAY = 2

    LocationPurpose = (
        (BILLING, 'Billing'),
        (POST, 'Post'),
        (DISPLAY, 'Display'),
    )


class LocationType(metaclass=ABCMeta):
    def __init__(self):
        pass

    RESIDENTIAL = 0
    COMMERCIAL = 1

    LocationType = (
        (RESIDENTIAL, 'Residential'),
        (COMMERCIAL, 'Commercial'),
    )
