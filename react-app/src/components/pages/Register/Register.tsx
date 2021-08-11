import React, { useState } from 'react';
import { withRouter } from 'react-router-dom';
import styled from 'styled-components';
import axios from 'axios';

import Typography from '@material-ui/core/Typography';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';

const Container = styled.div`
    margin: 30px auto;
    text-align: center;
    width: 300px;
`;

const TextFieldsContainer = styled.div`
    display: flex;
    flex-direction: column;
`;

const ResultMessage = styled(Typography)`
    color: #ff0000;
`;

const ActionButtonsContainer = styled.div`
    text-align: center;
    margin-top: 20px;
`;

const apiBaseUrl = 'http://localhost:3030/api/user';

type Props = {
    history: any;
};

const Register = ({ history }: Props): React.ReactElement => {
    const [usernameTF, setUsernameTF] = useState('');
    const [emailTF, setEmailTF] = useState('');
    const [passwordTF, setPasswordTF] = useState('');
    const [password2TF, setPassword2TF] = useState('');
    const [returnMessage, setReturnMessage] = useState('');

    const registerUser = async () => {
        return await axios({
            method: 'POST',
            url: apiBaseUrl + '/register',
            data: {
                username: usernameTF,
                email: emailTF,
                password: passwordTF,
                password2: password2TF,
            },
        });
    };

    const handleRegisterUser = () => {
        registerUser()
            .then(({ data }) => {
                console.log(data);
                if (data.error) setReturnMessage('Error');
                else {
                    setReturnMessage('User Registered');
                    history.push('/login');
                }
            })
            .catch((error) => {
                console.log(error);
                setReturnMessage('Error');
            });
    };

    return (
        <Container>
            <Typography variant="h4">Register</Typography>
            <TextFieldsContainer>
                <TextField
                    label="Username"
                    value={usernameTF}
                    onChange={(event) => setUsernameTF(event.target.value)}
                />
                <TextField label="Email" value={emailTF} onChange={(event) => setEmailTF(event.target.value)} />
                <TextField
                    label="Password"
                    type="password"
                    value={passwordTF}
                    onChange={(event) => setPasswordTF(event.target.value)}
                />
                <TextField
                    label="Re-type Password"
                    type="password"
                    value={password2TF}
                    onChange={(event) => setPassword2TF(event.target.value)}
                />
            </TextFieldsContainer>
            {returnMessage && <ResultMessage>{returnMessage}</ResultMessage>}
            <ActionButtonsContainer>
                <Button color="primary" variant="contained" onClick={handleRegisterUser}>
                    Sign Up
                </Button>
            </ActionButtonsContainer>
        </Container>
    );
};

export default withRouter(Register);
