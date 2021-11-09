const continents = [
    {
        "_id": 1,
        "name": "전자제품"
    },
    {
        "_id": 2,
        "name": "가전제품"
    },
    {
        "_id": 3,
        "name": "남성의류"
    },
    {
        "_id": 4,
        "name": "여성의류"
    },
    {
        "_id": 5,
        "name": "식품"
    },
    {
        "_id": 6,
        "name": "공구"
    },
    {
        "_id": 7,
        "name": "반려동물용품"
    }

]

const price = [
    {
        "_id": 0,
        "name": "Any",
        "array": []
    },
    {
        "_id": 1,
        "name": "$0 to $199",
        "array": [0, 199]
    },
    {
        "_id": 2,
        "name": "$200 to $249",
        "array": [200, 249]
    },
    {
        "_id": 3,
        "name": "$250 to $279",
        "array": [250, 279]
    },
    {
        "_id": 4,
        "name": "$280 to $299",
        "array": [280, 299]
    },
    {
        "_id": 5,
        "name": "More than $300",
        "array": [300, 1500000]
    }
]




export {
    continents,
    price
}
