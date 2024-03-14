// Solo l'import ES6
import { Pool } from 'pg';

const pool = new Pool({
    user: 'user',
    host: 'localhost',
    database: 'nomedelDB',
    password: 'password',
    port: 5432,
});

pool.query('SELECT NOW()', (err, res) => {
    if (err) {
        console.error('Errore di query:', err.stack);
    } else {
        console.log('Risultato della query:', res.rows[0]);
    }
    pool.end();
});
