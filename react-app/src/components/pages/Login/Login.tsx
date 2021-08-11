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

    & .action-button {
        margin: 5px;
    }
`;

const apiBaseUrl = 'http://localhost:3030';

type Props = {
    history: any;
};

const LoginPage = ({ history }: Props): React.ReactElement => {
    const [usernameTF, setUsernameTF] = useState('');
    const [passwordTF, setPasswordTF] = useState('');
    const [loginError, setLoginError] = useState('');

    const login = async (username: string, password: string) => {
        return await axios({
            method: 'post',
            url: apiBaseUrl + '/auth/login-flask',
            auth: {
                username,
                password,
            },
        });
    };
    const loginWithCookies = async (username: string, password: string) => {
        return await axios({
            method: 'post',
            url: apiBaseUrl + '/auth/login-with-cookies',
            auth: {
                username,
                password,
            },
        });
    };

    const handleUsernameTF = (event: any) => {
        setUsernameTF(event.target.value);
    };
    const handlepasswordTf = (event: any) => {
        setPasswordTF(event.target.value);
    };
    const handleLogin = () => {
        loginWithCookies(usernameTF, passwordTF)
            .then(({ data }) => {
                // console.log(data.access_token);
                if (data.success === 1) history.push('/');
            })
            .catch(() => {
                setLoginError('Login Error');
            });
    };
    const handleSignUp = () => {
        history.push('/Register');
    };

    return (
        <Container>
            <Typography variant="h4">Login</Typography>
            <TextFieldsContainer>
                <TextField label="Username" value={usernameTF} onChange={handleUsernameTF} />
                <TextField label="Password" type="password" value={passwordTF} onChange={handlepasswordTf} />
            </TextFieldsContainer>
            {loginError && <ResultMessage variant="caption">{loginError}</ResultMessage>}
            <ActionButtonsContainer>
                <Button className="action-button" color="primary" variant="contained" onClick={handleLogin}>
                    Login
                </Button>
                <Button className="action-button" color="primary" variant="outlined" onClick={handleSignUp}>
                    Sign Up
                </Button>
            </ActionButtonsContainer>
        </Container>
    );
};

export default withRouter(LoginPage);
