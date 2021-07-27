import React, { useState, useEffect } from 'react'
import styled from 'styled-components'
import axios from 'axios'

import Typography from '@material-ui/core/Typography'
import TextField from '@material-ui/core/TextField'
import Button from '@material-ui/core/Button'
import { default as MatCard } from '@material-ui/core/Card'
import CardHeader from '@material-ui/core/CardHeader'
import CardContent from '@material-ui/core/CardContent'

const Container = styled.div`
    margin: 0 5px;
`

const FilterContainer = styled.div`
    text-align: center;
`

const CardContainer = styled.div`
    text-align: center;
    display: flex;
    flex-direction: row;
`

const Card = styled(MatCard)`
    width: 300px;
    margin: 5px;
`

const ShowsPage = () => {
    const [searchKeyword, setSearchKeyword] = useState('');
    const [showsData, setShowsData] = useState([]);

    const handleSearchKeywordChange = (event) => {
        setSearchKeyword(event.target.value)
    };

    useEffect(() => {
        getAllShows();
    },[]);

    useEffect(() => {
        console.log(showsData);
    },[showsData]);

    const getAllShows = async () => {
        await axios.get('http://localhost:3030/show/').then(({data}) => {
            setShowsData(data.data);
        });
    }

    const searchShow = async () => {
        await axios.get('http://localhost:3030/show/search/' + searchKeyword).then(({data}) => {
            setShowsData(data.data);
        });
    }

    return (
        <Container>
            <Typography variant='h1'>Shows</Typography>
            <FilterContainer>
                <TextField id='search-keyword' name='Search' label='Search' value={searchKeyword} onChange={handleSearchKeywordChange} />
                <Button variant='contained' color='primary' onClick={searchShow}>Search</Button>
            </FilterContainer>
            <CardContainer>
                {
                    showsData.map(({ id, title, director, cast, type }) => (
                        <Card key={id}>
                            <CardHeader title={title} />
                            <CardContent>
                                <Typography variant='body1'>Director: {director}</Typography>
                                <Typography variant='body1'>Casts: {cast.join(', ')}</Typography>
                                <Typography variant='body1'>Type: {type}</Typography>
                            </CardContent>
                        </Card>
                    ))
                }
                {/* <Card>
                    <CardHeader title={title} />
                    <CardContent>
                        <Typography variant='body1'>Testing</Typography>
                    </CardContent>
                </Card> */}
            </CardContainer>
        </Container>
    )
}

export default ShowsPage
