module.exports = {
  "apps": [{
    "name": "crypttops-bybit-webhook-service",
    "script": "app.py",
    "args": [],
    "instances": "1",
    "wait_ready": true,
    "autorestart": false,
    "max_restarts": 5,
    "interpreter" : ".venv/bin/python",
},
{
  "name": "crypptttops-bybit-telegram-bot-service",
  "script": "tradetelegrambot.py",
  "args": [],
  "instances": "1",
  "wait_ready": true,
  "autorestart": false,
  "max_restarts": 5,
  "interpreter" : ".venv/bin/python",
}

],

  // deploy : {
  //   production : {
  //     user : 'SSH_USERNAME',
  //     host : 'SSH_HOSTMACHINE',
  //     ref  : 'origin/master',
  //     repo : 'GIT_REPOSITORY',
  //     path : 'DESTINATION_PATH',
  //     'pre-deploy-local': '',
  //     'post-deploy' : 'npm install && pm2 reload ecosystem.config.js --env production',
  //     'pre-setup': ''
  //   }
  // }
};
