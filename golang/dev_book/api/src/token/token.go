package token

import (
	"api/src/config"
	"time"

	"github.com/golang-jwt/jwt"
)

func CreateToken(userID uint64) (string, error) {
	permissions := jwt.MapClaims{
		"authorized": true,
		"exp": time.Now().Add(time.Hour * 6).Unix(),
		"userID": userID,
	}
	token := jwt.NewWithClaims(jwt.SigningMethodHS256, permissions)
	return token.SignedString([]byte(config.SecretKey))
}