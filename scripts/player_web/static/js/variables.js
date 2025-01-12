
//------------------------------------
// keycode映射按键
//------------------------------------
var key_map = {
	87:"w",
	83:"s",
	65:"a",
	68:"d",
	81:"q",
	69:"e",
	82:"reset",
	27:"esc",
	79:"o"

}

//------------------------------------
// 按键是否被按下
//------------------------------------
var active_map = {
	"w":false,
	"s":false,
	"a":false,
	"d":false,
	"q":false,
	"e":false,
	"o":false,
	"shoot":false,
	"autoAim":false,
	"reset":false,
	"movementX":0,
	"movementY":0
}

//------------------------------------
// 发送间隔
//------------------------------------
var send_freq = 60

//------------------------------------
// 用于调整yaw的灵敏度， 越大越不灵敏
//------------------------------------
var yaw_factor = 800

//------------------------------------
// 越大越不灵敏
//------------------------------------
var pitch_factor = 800

var my_robot
